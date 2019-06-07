import re
from argparse import Namespace
from base64 import decodebytes, encodebytes
from collections import Counter

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)


def parse_signature_header(s):
    """
    Parse a given `Signature` header into a dict.
    :param s: the `Signature` header value.
    :return: a dict representing the Signature parameters
    """
    parameters = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', s)
    parameters = [x.split("=", 1) for x in parameters]

    # TODO validate parameters' name.
    c = Counter(x[0] for x in parameters)
    duplicate_params = [k for k, v in c.items() if v > 1]
    if duplicate_params:
        raise ValueError("Duplicate headers %r" % c)

    # TODO validate parameters' content.
    return {k: v.strip('"') if isinstance(v, str) else v for k, v in parameters}


def serialize_signature(signature_parameters):
    signature_header = f"Signature: "
    for p, v in signature_parameters.items():
        if isinstance(v, str):
            v = f'"{v}"'
        signature_header += f"{p}={v},"

    # remove last comma.
    return signature_header.strip(",")


def load_pubkey(x509_pem):
    """
    Load a PEM-encoded public key in a python-cryptography object.
    :param x509_pem: a PEM-encoded public key
    :return: A python-cryptography public key.
    """
    return load_pem_public_key(x509_pem, default_backend())


def load_key(key):
    """
    Load a PEM-encoded private key in a python-cryptography object.
    :param x509_pem: a PEM-encoded private key
    :return: A python-cryptography public key.
    """

    return load_pem_private_key(key, password=None, backend=default_backend())


def sign_string(private_key, signature_string: bytes):
    # HTTP Headers SHOULD only use ascii
    return sign_bytes(private_key, signature_string.encode("ascii"))


def verify_string(public_key, signature_string: str, b64_signature: str):
    # HTTP Headers SHOULD only use ascii
    return verify_bytes(public_key, signature_string.encode("ascii"), b64_signature)


def sign_bytes(private_key, signature_bytes: bytes):
    """
    Sign a byte sequence with the given private key.
    :param private_key:
    :param signature_bytes:
    :return: a base-64 encoded signature of `signature_bytes`
    """
    signature = private_key.sign(
        signature_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    return encodebytes(signature).strip().decode("ascii")


def verify_bytes(public_key, signature_bytes: bytes, b64_signature: str):
    """
    Verify that a base64 encoded signature matches the `signature_bytes`.
    :param public_key:
    :param signature_bytes:
    :param b64_signature:
    :return: None on success, an exception on failure.
    """
    public_key.verify(
        decodebytes(b64_signature.encode("ascii")),
        signature_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    return True
