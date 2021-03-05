Signing HTTP Messages
=====================

This project is the main work area for the [Signing HTTP Messages draft
standard](https://datatracker.ietf.org/doc/draft-cavage-http-signatures/).

The standard aims to provide a way for senders of HTTP messages - both
requests and respnses - to digitally sign specified headers in a manner
compatible with existing HTTP implementations.

# Motivation

Many schemes exist to protect data objects that may be transported as the
payload of a HTTP message. These include JWS, XML Signatures, and detached
sgnatures in multipart messages using e.g. GPG.

However there is no accepted mechanism to provide protection to the HTTP
message as a whole, and especially within a single HTTP request/response
session.

With this specification, a sender (HTTP client or server) can attach a
signature to any HTTP message, allowing any recipient to read the signature
and verify the integrity of the message and detect tampering.

# Operation

The underlying mechanisms of the protocol are rather simple:

- A set of a HTTP message's headers are "canonicalized" (transformed to a
  standard representation) into a single string
- The canonicalized string (hash) is digitally signed with either a shared
  secret, or a private key
- The digital signature is included as a header in the message it signed,
  along with parameters explaining how the signature was formulated

Using the canonicalization method and the provided header, any application
reading the HTTP message, and (using either the shared secret or the
corresponding public key as necessary) verify:

- The integrity of the message (it has not been altered since being signed)
- The identity of the signer if the key can be associated with the identity
  of the signer

The protocol, operates in one of two modes, though the core mechanism of
generating and verifiying signatures is the same in both:

- The `Signature` header, which can add a signature to any HTTP message
  (request or response)
- The "Signature HTTP Authentication Scheme" which is used in HTTP requests
  to authorize access to a resource.

# Contributing

This standard is under active development, and contributions are welcome.

Please review the [Contributing Guide](./CONTRIBUTING.md) to see how you
can participate, as well as learn about the principles of the project to
help the process along.

The specification itself is documented in the file [index.xml](index.xml).
This is a standard representation for IETF standards, which is then rendered
in other representations including text, HTML and PDF as needed.

The Python tool [XML Copy Editor](http://xml-copy-editor.sourceforge.net/)
can be used to edit and validate the XML file in a GUI, while the tool
``xml2rfc`` is used to both check the integrity of the edited XML file and
render it in various formats locally. The tool is available
[online](https://xml2rfc.tools.ietf.org/) and as
a [Python package](https://pypi.org/project/xml2rfc/).

# Copyright Notice

Copyright (c) 2019 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the [IETF Trust's Legal Provisions
Relating to IETF Documents](https://trustee.ietf.org/license-info) in
effect on the date of publication of this document.  Please review these
documents carefully, as they describe your rights and restrictions with
respect to this document.
