import logging
from pathlib import Path

import yaml

from utils import (
    load_key,
    load_pubkey,
    parse_signature_header,
    serialize_signature,
    sign_string,
    verify_string,
)

tests = yaml.safe_load(Path("examples.yaml").read_text())

PRIVATE_KEY = load_key(Path("rsa.key").read_bytes())
PUBLIC_KEY = load_pubkey(Path("rsa.pub").read_bytes())

log = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def test_sign_verify():
    s = "sample"
    assert verify_string(PUBLIC_KEY, s, sign_string(PRIVATE_KEY, s))


def test_generate_signatures():
    for test in tests['examples']:
        parameters = test["parameters"]

        # If a valid signature is provided, just validate it
        # otherwise generate and output a new signature
        parameters["signature"] = parameters.get("signature") or sign_string(
            PRIVATE_KEY, test["signature_string"]
        )
        signature_header = serialize_signature(parameters)
        signature_dict = parse_signature_header(signature_header.strip("Signature: "))
        for x in parameters.keys():
            assert x in signature_dict

        verify_string(PUBLIC_KEY, test["signature_string"], signature_dict["signature"])
        log.warning("---Test:  %r", test["name"])
        log.warning("Output:  %r", signature_header)
        print("Signature: %s" % yaml.dump(parameters, default_flow_style=0))


if __name__ == "__main__":
    test_sign_verify()
    test_generate_signatures()
