import requests

LLM_URL="http://localhost:11434/api/generate"

def get_llm_response(message:str,memories:list[str]):
    context = "\n".join(memories)
    payload = {
        "model": "llama3",
        "prompt": f"""
            You are a helpful assistant.

            Use the memory below ONLY if relevant.

            Memories:
            {context}

            User Question:
            {message}

            Answer clearly and naturally.
            """,
        "stream": False
    }
    response = requests.post(LLM_URL,json=payload)
    return response.json()['response']