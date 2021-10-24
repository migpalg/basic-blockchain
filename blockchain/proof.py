import hashlib

HASH_TARGET = '0000'


def is_valid_hash_target(current_hash: str) -> bool:
    """
    Validates if a generated hex is valid for the hash target
    :param current_hash: hash to validate
    """
    return current_hash[:len(HASH_TARGET)] == HASH_TARGET


def proof_of_work(previous_proof: int) -> int:
    """
    Generates a new value for proof of work for the next block
    :param previous_proof: Proof of work of the previous block
    """
    new_proof = 1
    proof_found = False

    while not proof_found:
        hash_operation = hashlib.sha256(
            str(new_proof**2 - previous_proof**2).encode()).hexdigest()

        if is_valid_hash_target(hash_operation):
            proof_found = True
        else:
            new_proof = new_proof + 1

    return new_proof
