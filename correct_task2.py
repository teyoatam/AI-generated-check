import re
from typing import Iterable
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
def count_valid_emails(emails: Iterable) -> int:
    if emails is None:
        return 0
    
    count = 0
    for email in emails:
        if isinstance(email, str) and _EMAIL_RE.match(email):
            count += 1
    return count