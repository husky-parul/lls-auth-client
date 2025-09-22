from fastapi import FastAPI
from lls_auth_client.routes import invoke
from lls_auth_client.config import settings

app = FastAPI(
    title="LLS Auth Client",
    description="FastAPI client with Keycloak OAuth2 for Llama Stack",
    version="0.1.0",
    debug=settings.DEBUG,
)

# include routes
app.include_router(invoke.router, prefix="/api", tags=["lls"])

@app.get("/health")
async def health():
    return {"status": "ok"}
