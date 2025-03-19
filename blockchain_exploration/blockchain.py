import hashlib
import json


def hash(message: str = "") -> str:
    if isinstance(message, str):
        message = json.dumps(message, sort_keys=True)
    return hashlib.sha256(str(message).encode("utf-8")).hexdigest()
