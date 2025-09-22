import httpx
from lls_auth_client.auth import keycloak_auth
from lls_auth_client.config import settings


async def send_prompt(prompt: str) -> dict:
    """
    Send a prompt to Ollama with Keycloak token attached.
    Returns the JSON response.
    """
    token = keycloak_auth.get_token()

    headers = {
        "Authorization": f"Bearer {token}",  # still included for ZT / future checks
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama3.2:3b",  # matches the one you ran with `ollama run`
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False  # easier to handle full response
    }

    url = f"{settings.LLS_BASE_URL}/api/chat"  # <-- Ollama native endpoint

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
