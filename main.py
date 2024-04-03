from fastapi import FastAPI
import uvicorn
from mylib.logic import (
    wiki as wiki_logic,
    search_wiki,
    phrase as wiki_phrases,
)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """API to search given value in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}/{length}")
async def wiki(name: str, length: int):
    """API to retrieve wikipedia page content"""

    result = wiki_logic(name, length)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """API to retrieve wikipedia page content and count phrases"""

    result = wiki_phrases(name)
    return {"results": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
