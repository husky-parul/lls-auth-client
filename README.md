# LLS Auth Client

This project demonstrates step-by-step how to build a secure inference client for **Llama Stack** using **FastAPI** and **Keycloak OAuth2**, with **Ollama** as the inference provider.

---

## 🎯 Project Modules

### [Module 1](./docs/MODULE1.md)
- Set up FastAPI client with Keycloak OAuth2.
- Connect directly to **Ollama**.
- Implements the **basic OAuth flow**:  
  FastAPI → Keycloak → Ollama.

### [Module 2](./docs/MODULE2.md)
- Introduce **Llama Stack** as a secure gateway in front of Ollama.
- Configure `run.yaml` with Keycloak as OAuth provider.
- FastAPI client obtains JWT → sends to Llama Stack → Llama Stack authenticates with Keycloak → forwards to Ollama.
- At this stage, **no tool calls** are enabled. Only authentication + text inference.

---

## 📚 Next
In the next module, you will set up the FastAPI client with Keycloak OAuth2 and connect it directly to Ollama for the basic authentication flow.

- 👉 [Go to Module 1 »](./docs/MODULE1.md)
