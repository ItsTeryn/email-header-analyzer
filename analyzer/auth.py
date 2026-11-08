import re

CHECKS = ["spf", "dkim", "dmarc"]
AUTH_PATTERN = re.compile(r"\b(spf|dkim|dmarc)=(\w+)", re.IGNORECASE)


def get_auth_results(msg):
    """Read the SPF, DKIM, and DMARC results from the Authentication-Results header."""
    results = {check: "not found" for check in CHECKS}

    for header in msg.get_all("Authentication-Results", []):
        text = " ".join(str(header).split())

        for check, result in AUTH_PATTERN.findall(text):
            check = check.lower()
            if results[check] == "not found":
                results[check] = result.lower()

    return results
