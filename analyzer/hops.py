import re

FROM_PATTERN = re.compile(r"\bfrom\s+(\S+)", re.IGNORECASE)
BY_PATTERN = re.compile(r"\bby\s+(\S+)", re.IGNORECASE)
IP_PATTERN = re.compile(r"\[(\d{1,3}(?:\.\d{1,3}){3})\]")


def get_hops(msg):
    """Return the Received hops in order, from where the email started to where it landed."""
    received = msg.get_all("Received", [])
    hops = []

    for number, line in enumerate(reversed(received), start=1):
        line = " ".join(str(line).split())

        from_match = FROM_PATTERN.search(line)
        by_match = BY_PATTERN.search(line)
        ip_match = IP_PATTERN.search(line)

        hops.append({
            "hop": number,
            "from": from_match.group(1) if from_match else "(unknown)",
            "by": by_match.group(1) if by_match else "(unknown)",
            "ip": ip_match.group(1) if ip_match else "(none)",
        })

    return hops
