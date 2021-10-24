import hashlib
from .block import Block
from .proof import is_valid_hash_target


class Chain:
    def __init__(self) -> None:
        self.chain: list[Block] = []
        self.add_block(proof=1, previous_block='0'*64)

    def add_block(self, proof: int, previous_block: str) -> dict:
        block = Block(
            index=len(self.chain) + 1,
            proof=proof,
            previous_block=previous_block)
        self.chain.append(block)
        return block.to_dict()

    def get_chain(self) -> list[dict]:
        return list(map(lambda block: block.to_dict(), self.chain))

    def validate(self) -> bool:
        previous_hash = self.chain[0].hash_self()
        previous_proof = self.chain[0].proof

        for block in self.chain[1:]:
            if block.previous_block != previous_hash:
                return False

            hash_operation = hashlib.sha256(
                str(block.proof**2 - previous_proof**2).encode()).hexdigest()

            if not is_valid_hash_target(hash_operation):
                return False

            previous_hash = block.hash_self()
            previous_proof = block.proof

        return True

    def get_last_block(self) -> Block:
        return self.chain[-1]
