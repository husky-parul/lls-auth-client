import os
from dotenv import load_dotenv

# Load .env file into environment
load_dotenv()

class Settings:
    # Keycloak
    KEYCLOAK_BASE_URL: str = os.getenv("KEYCLOAK_BASE_URL", "http://localhost:8080")
    KEYCLOAK_REALM: str = os.getenv("KEYCLOAK_REALM", "myrealm")
    KEYCLOAK_CLIENT_ID: str = os.getenv("KEYCLOAK_CLIENT_ID", "lls-client")
    KEYCLOAK_CLIENT_SECRET: str = os.getenv("KEYCLOAK_CLIENT_SECRET", "super-secret")
    KEYCLOAK_TOKEN_URL: str = (
        f"{KEYCLOAK_BASE_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
    )

    # Llama Stack (LLS)
    LLS_BASE_URL: str = os.getenv("LLS_BASE_URL", "http://localhost:11434")
    LLS_CHAT_ENDPOINT: str = os.getenv("LLS_CHAT_ENDPOINT", "/v1/chat/completions")

    # General
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
