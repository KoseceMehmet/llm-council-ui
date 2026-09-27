import httpx
import json

def resolve_api_key(api_keys: dict, provider: str) -> str:
    """Dynamically resolves API key or endpoint URL based on normalized provider name."""
    provider_lower = provider.lower()
    
    # Exact or partial key matching
    for key_name, value in api_keys.items():
        if provider_lower in key_name or key_name in provider_lower:
            return value
    return ""

async def fetch_llm_response(provider: str, model_name: str, system_prompt: str, user_prompt: str, context: str = "", api_keys: dict = {}) -> str:
    full_prompt = f"{user_prompt}\n\n[ATTACHED CONTEXT / LOGS]:\n{context}" if context else user_prompt
    resolved_key = resolve_api_key(api_keys, provider)
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            if provider == "OpenRouter":
                headers = {
                    "Authorization": f"Bearer {resolved_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": full_prompt}
                    ]
                }
                response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                
            elif provider == "Groq":
                headers = {
                    "Authorization": f"Bearer {resolved_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": full_prompt}
                    ]
                }
                response = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

            elif provider == "Ollama (Local)":
                endpoint = resolved_key if resolved_key else "http://localhost:11434"
                url = f"{endpoint}/api/generate"
                payload = {
                    "model": model_name,
                    "prompt": f"{system_prompt}\n\nUser: {full_prompt}",
                    "stream": False
                }
                response = await client.post(url, json=payload)
                if response.status_code == 200:
                    return response.json().get("response", "Empty response received.")

            elif provider == "OpenAI":
                headers = {
                    "Authorization": f"Bearer {resolved_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": full_prompt}
                    ]
                }
                response = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"[API ERROR {response.status_code}]: {response.text}"
                
    except Exception as exc:
        return f"[CONNECTION EXCEPTION]: {str(exc)}"
