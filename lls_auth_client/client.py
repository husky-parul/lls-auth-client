import httpx
from lls_auth_client.auth import keycloak_auth
from lls_auth_client.config import settings


async def send_prompt(prompt: str) -> dict:
    """
    Send a prompt to Llama Stack's inference API with Keycloak token.
    Returns the JSON response.
    """
    token = keycloak_auth.get_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "model_id": "llama3.2:3b",  # must match INFERENCE_MODEL in run.yaml
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    url = f"{settings.LLS_BASE_URL}{settings.LLS_CHAT_ENDPOINT}"

    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()
