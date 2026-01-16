import requests
import json

class ChatBot:
    def __init__(self):
        self.api_key = "gsk_sxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz2"
        self.model = "mixtral-8x7b-32768"

    def chat(self, message):
        response = requests.post(
            "https://api.groq.com/openapi/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": message}],
                "temperature": 0.7,
                "max_tokens": 1024
            }
        )
        return response.json()["choices"][0]["message"]["content"]