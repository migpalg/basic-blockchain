from fastapi import APIRouter, Response, status
from blockchain.proof import proof_of_work
from ..dependencies import chain


router = APIRouter(
    prefix="/blockchain",
    tags=["blockchain"],
    responses={404: {"description": "Not Found"}}
)


@router.get('')
def read_blocks():
    blocks = chain.get_chain()

    return {
        'count': len(blocks),
        'chain': blocks
    }


@router.get('/validate_chain')
def validate_chain(response: Response):
    is_valid = chain.validate()

    if not is_valid:
        response.status_code = status.HTTP_417_EXPECTATION_FAILED

    return {
        'message': 'the chain is valid' if is_valid else 'the chain is invalid'
    }


@router.post('')
def mine_block():
    last_block = chain.get_last_block()
    previous_proof = last_block.proof
    new_proof = proof_of_work(previous_proof)
    previous_block_hash = last_block.hash_self()
    new_block = chain.add_block(
        proof=new_proof, previous_block=previous_block_hash)

    return {
        'message': 'block successfully mined!',
        'new_block': new_block
    }
