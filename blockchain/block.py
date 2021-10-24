from datetime import datetime
import hashlib
import json


class Block:
    def __init__(self, index: int, proof: int, previous_block: str) -> None:
        self.index = index
        self.proof = proof
        self.previous_block = previous_block
        self.timestamp = str(datetime.now())

    def hash_self(self):
        self_dict = self.to_dict()
        raw_json = json.dumps(self_dict, sort_keys=True)
        return hashlib.sha256(raw_json.encode()).hexdigest()

    def to_dict(self) -> dict:
        return {
            'index': self.index,
            'previous_block': self.previous_block,
            'proof': self.proof,
            'timestamp': self.timestamp,
            'data': None
        }
