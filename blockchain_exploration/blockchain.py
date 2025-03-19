import hashlib
import json
import sys


def hash(message: str = "") -> str:
    if isinstance(message, str):
        message = json.dumps(message, sort_keys=True)

    if sys.version_info.major == 2:
        return hashlib.sha256(message).hexdigest()
    else:
        return hashlib.sha256(str(message).encode("utf-8")).hexdigest()
