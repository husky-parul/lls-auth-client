import time
import httpx
from lls_auth_client.config import settings


class KeycloakAuth:
    """
    Handles client credentials flow against Keycloak.
    Caches the token until it's close to expiry.
    """

    def __init__(self):
        self._access_token: str | None = None
        self._expires_at: float = 0.0

    def get_token(self) -> str:
        """Return a valid access token, refreshing if expired."""
        if self._access_token and time.time() < self._expires_at:
            return self._access_token
        return self._fetch_token()

    def _fetch_token(self) -> str:
        """Fetch a new token from Keycloak using client credentials."""
        data = {
            "grant_type": "client_credentials",
            "client_id": settings.KEYCLOAK_CLIENT_ID,
            "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        }

        try:
            response = httpx.post(
                settings.KEYCLOAK_TOKEN_URL,
                data=data,
                timeout=10.0,
            )
            response.raise_for_status()
        except httpx.RequestError as e:
            raise RuntimeError(f"Token request failed: {e}") from e
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"Keycloak returned error: {e.response.text}") from e

        token_response = response.json()
        access_token = token_response.get("access_token")
        expires_in = token_response.get("expires_in", 60)

        if not access_token:
            raise RuntimeError("Keycloak did not return an access token")

        # Cache token slightly before it expires
        self._access_token = access_token
        self._expires_at = time.time() + expires_in - 10
        return access_token


# Singleton instance for reuse
keycloak_auth = KeycloakAuth()
