"""Token hashing helpers for refresh-token persistence."""

import hashlib


def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()
