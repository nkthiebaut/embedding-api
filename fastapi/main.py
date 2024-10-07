from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")


class TextInput(BaseModel):
    text: str


@app.post("/embed")
async def get_embedding(input: TextInput):
    try:
        embedding = model.encode(input.text)
        return {"embedding": embedding.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the embedding API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
