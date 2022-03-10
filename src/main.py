from fastapi import FastAPI
from pkg.giphy import giphySearch

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{search}")
async def root():
    return {"message": "Hello World"}


