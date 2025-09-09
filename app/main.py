from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.clients.client import client_question
from app.schemas.schemas import Question, Response

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.post("/question", response_model=Response)
async def question(input_data: Question):
    try:
        response = await client_question(input_data.content)
        result = {"content": response}
        return Response(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")
