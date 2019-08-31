# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
XML2RFCBIN    = ~/.local/bin/xml2rfc
RFC           = draft-cavage-http-signatures
RFCXML        = ./index.xml

html: Makefile
	@$(XML2RFCBIN) --html "$(RFCXML)" -o "./$(RFC).xml"

text: Makefile
	@$(XML2RFCBIN) --text "$(RFCXML)" -o "./$(RFC).txt"

