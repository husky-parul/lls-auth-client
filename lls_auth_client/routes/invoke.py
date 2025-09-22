from fastapi import APIRouter
from lls_auth_client.client import send_prompt

router = APIRouter()

@router.post("/invoke")
async def invoke(payload: dict):
    prompt = payload.get("prompt")
    if not prompt:
        return {"error": "Missing prompt"}

    result = await send_prompt(prompt)
    return result
