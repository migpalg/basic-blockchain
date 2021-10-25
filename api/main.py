from fastapi import FastAPI, Depends
from .routers import blockchain


app = FastAPI()


app.include_router(blockchain.router)
