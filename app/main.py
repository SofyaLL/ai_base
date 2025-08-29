from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse

from app.clients.client import client_question

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.post("/question", response_class=JSONResponse)
async def question(text: str = Query(max_length=20)):
    try:
        response = await client_question(text)
        results = {"text": response}
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")
