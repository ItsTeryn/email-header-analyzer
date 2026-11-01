from email import policy
from email.parser import BytesParser

FIELDS = ["From", "To", "Subject", "Date", "Return-Path", "Reply-To", "Message-ID"]


def load_header(path):
	"""Read a header file and turn it into an email object."""
	with open(path, "rb") as f:
		return BytesParser(policy=policy.default).parse(f, headersonly=True)


def get_basic_fields(msg):
	"""Pull out the main fields. Use '(not found)' if one is missing."""
	return {name: msg.get(name, "(not found)") for name in FIELDS}
