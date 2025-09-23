# LLS Auth Client

A FastAPI client that uses **Keycloak OAuth2** for secure access to **Ollama (Llama models)**.  
Implements the client credentials flow to fetch a token, then forwards prompts to Ollama’s native API.

---

## ⚡ Requirements
- Python **3.12**
- [Ollama](https://ollama.com/) installed & running
- Keycloak running (e.g. in KinD or Docker)
- `uvicorn`, `fastapi`, `httpx`, `python-dotenv`

---

## 🛠 Setup

### 1. Clone repo & create venv
```bash
git clone <your-repo-url>
cd lls-auth-client
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Keycloak

- Create realm: `lls-auth`

- Create client: `lls-client`

- Client authentication: `ON`

- Service accounts enabled: `ON`

- Copy the client secret from the Credentials tab

### 3. Fill .env

```
# Keycloak
KEYCLOAK_BASE_URL=http://localhost:8080
KEYCLOAK_REALM=lls-auth
KEYCLOAK_CLIENT_ID=lls-client
KEYCLOAK_CLIENT_SECRET=<your-client-secret>

# Ollama
LLS_BASE_URL=http://localhost:11434
LLS_CHAT_ENDPOINT=/api/chat

DEBUG=true
```

### 4. Running

#### 4.1. Start ollama
```
ollama run llama3.2:3b --keepalive 180m
```

#### 4.2. Start FastAPI
```
uvicorn lls_auth_client.main:app --reload
```

💬 Example Prompt
```
curl -X POST http://127.0.0.1:8000/api/invoke \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello Llama, how are you?"}'
```

Example response

```
{
  "model": "llama3.2:3b",
  "message": {
    "role": "assistant",
    "content": "Hello! I'm ready to help you."
  },
  "done": true
}
```

This is the basic OAuth flow. 

## 🔐 OAuth + Llama Stack Flow

The system now integrates FastAPI, Keycloak, Llama Stack, and Ollama into a secure inference pipeline:

The FastAPI client obtains a JWT from Keycloak using the client credentials flow.

FastAPI forwards the user prompt to Llama Stack, attaching the JWT.

Llama Stack validates the token against Keycloak (as configured in run.yaml).

Once authenticated, Llama Stack forwards the prompt to Ollama, which performs the model inference.

The response flows back through Llama Stack to the FastAPI client, and finally to the user.

At this stage, the /api/invoke route is powered by Llama Stack for authentication and inference.

> 👉 Note: Tool calls have not been enabled yet — this flow handles only basic OAuth authentication and text inference.

## 📚 Next
In the next module, you will introduce **Llama Stack** as a secure gateway in front of Ollama, with Keycloak configured as the OAuth provider.
- 👉 [Go to Module 2 »](./docs/MODULE2.md)
- ⬆️ [Back to README](../README.md)