# HTTP Signatures examples

This directory contains python code samples to create, verify and 
validate the examples used in the spec.

To run and show all examples data, just run:

        tox

## Requirements

Python 3.6+ with `pip` and `tox`.

## Files

The public and private keys referenced in [Appendix C](https://tools.ietf.org/html/draft-cavage-http-signatures-11#appendix-C):

- rsa.key, rsa.pub

## Examples

Every example is defined in [example.yaml](example.yaml) which contains 
a list of testable entries.

Each entry refers the spec paragraph, the signature string and the required
parameters and associate signature string.

If `parameters.signature` is not defined, the `example.py` creates a new one.


```
- name: Default Test
  url: https://tools.ietf.org/html/draft-cavage-http-signatures-11#appendix-C.1
  signature_string: >-
    date: Sun, 05 Jan 2014 21:31:40 GMT
  parameters:
    keyId: Test
    algorithm: rsa-sha256
    signature: |-
      e2Jwiqw6NYMaLpa2O+zYHfYc0XeLdjCvp9+sO53ahux9YlcU+EFi/P78075S+Qmh2ZbFai0h0/XO
      Muvzzjl2NwXIzYm22Ew4sculMDgv/tiowY76We6fBtBvr/CLZgNq5gXJJgOR7B7zdNfoJW6VXu/w
      kbkBHM0665wazTJayX0=
```


