Signing HTTP Messages Contribution Guide
========================================

This specification is under active development, and the more participants
we get the better for everyone. We want this specification to be a
useful addition to the ecosystem of the Internet, so it needs to be
readable, useful and effective.

You can contribute to the project by looking at the
[open issues](https://github.com/w3c-dvcg/http-signatures/issues) and join
a discussion, or raise a new issue if you have a bug or new feature
suggestion.

First though, take a look at the guiding principles of the project:

# Principles

## Platform, Language & Transport neutrality

This protocol is meant to provide a technical mechanism to produce and
verify digital signatures of HTTP Messages in a platform-agnostic way

- The protocol should not be overly specific with a particular
  implementation, language, runtime or framework.
  The protocol should work the same way for all.

- The protocol must be independent of the transport and any security
  mechanisms implemented there e.g. client & server TLS certificates.

## Simple and Compatible

- This specification should comply fully with the state of HTTP except where
compliance would introduce security concerns.

  - If HTTP does or permits something, this protocol should allow it to be
  signed.

  - This means we also support things that present for legacy reasons or
    perhaps don't seem like an obviously good idea, unless there is a good
    (especially security) reason not to.

- Any implementation that does not recognise or support this protocol should
  be able to ignore any signature header safely.

- The specification should avoid wherever possible any aspects requiring
  negotiation or agreement between parties. Out-of-band specification of
  permissible parameters, keys etc should be relied upon unless critical to
  security or functionality.

- This specification must not apply new interpretations to existing
  concepts and terms

- This specification should be simple enough for non-specialists to
  understand and recognise the core concepts, allowing them to make informed
  choices on how it can/should be used, while also specific enough that
  implementers can unambiguously understand how to produce and verify a
  signature safely and effectively.

# What You See is What You Sign

- Signatures serve an immediate purpose to authenticate and verify a
  HTTP message at the point it is received and processed, so the protocol
  should provide a mechanism to determine the timeliness of a signature

- Signatures may serve an after-the-fact purpose to be able to verify that a
  request or response was properly verified at some point in the past
  (auditing)

- To serve both the above purposes, signatures should be verifiable given
  the information available at that time. Signatures should not rely on
  information not present in a given message except for the secrets used.