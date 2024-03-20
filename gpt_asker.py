import requests
import json

import config


def call_gpt4(prompt):
    url = "https://api.openai.com/v4/completions"
    headers = {
        "Authorization": f"Bearer {config.GPT_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "text-davinci-003",  # Или другая модель GPT-4, если доступна
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 150,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get("choices", [{}])[0].get("text", "").strip()
    else:
        return "Ошибка при выполнении запроса к API GPT-4"


if __name__ == '__main__':

    # Пример использования:
    prompt = "Привет, я подключился? Запрос успешен?"

    print(call_gpt4(prompt))
