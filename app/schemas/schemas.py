from pydantic import BaseModel, Field


class Question(BaseModel):
    content: str = Field(
        min_length=5, max_length=30, description="Query text to chat bot"
    )


class Response(BaseModel):
    content: str = Field(description="Otput from llm")
