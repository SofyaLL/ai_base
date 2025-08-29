from openai import AsyncOpenAI

from app.settings import settings

client = AsyncOpenAI(
    api_key=settings.openai_api_key,
)


async def client_question(text: str) -> str:
    response = await client.responses.create(model="gpt-5-nano", input=text)
    return response.output_text
