"""Empty test, just to raise warning"""

from blockchain_exploration.blockchain import hash
import pytest


@pytest.mark.parametrize(
    "message, hash_value",
    [
        ("ahoj", "36bc2a9f06716c2783264428380e723a58dc5e8883fa75ef060f6b9b382b49dd"),
        ("nope", "9b4e7a802b0bd7e5e84bb9876a454cfcd4f697120e553fd7a30ecb8ade094852"),
    ],
)
def test_hash(message: str, hash_value: str) -> None:
    hashed_msg = hash(message=message)
    assert hashed_msg == hash_value
