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

- The protocol should not be overly specific with a particular implementation,
  language, runtime or framework. The protocol should work the same way for
  all.

- The protocol must be independent of the transport and any security
  mechanisms implemented there e.g. client & server TLS certificates.

## Simple and Compatible

This protocol should comply fully with the state of HTTP except where
compliance would introduce security concerns. Don't re-interperet existing
definitions or protocols or modify the meanings of established ideas.

- If HTTP does or permits something, this protocol should allow it to be signed.
  - This means we also support things that are there for legacy reasons or
  perhaps don't seem like an obviously good idea, unless there is a good
  (especially security) reason not to.
  
- Any implementation that does not recognise or support this protocl should
  be able to ignore any signature header safely.

- The specification should avoid wherever possible any aspects requiring negotiation or agreement on parameters.

- This specification must not apply new interpretations to existing concepts and terms


From Manu:

* Don't break the ecosystem, stay backwards compatible.
