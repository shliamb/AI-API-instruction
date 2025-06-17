import requests
from config import HOST, ACCESS_ID, API_KEY, VALUE_KEY

path_file = None

#path_file = "./uploads/image45.png"

url = f"http://{HOST}/api/claude/"

data = {
        ACCESS_ID: "08a898f3-e6dd-49c2-93a7-fff0abc7ad31",
        "user_content": "Что ты видишь?", # !
        "system_content": "Тебя зовут Ева",
        "model": "claude-3-haiku-20240307",
        #'assist_content': '[{"user": "Привет, меня зовут Алекс."}, {"assistant": "Очень приятно Алекс, я Ева."}, {"user": "Мне 40 лет."}, {"assistant": "Ты в самом расвете сил!"}]',
}

headers = {
    API_KEY: VALUE_KEY,
}

if path_file:
    with open(path_file, 'rb') as f:
        file = {'file': ('image45.png', f)}
        response = requests.post(url, headers=headers, data=data, files=file)
else:
    response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)

print(response)




















#{'id': 'msg_015mwuobJH1K1X3tiZYdzEtu', 'type': 'message', 'role': 'assistant', 'model': 'claude-3-5-sonnet-20241022', 'content': [{'type': 'text', 'text': 'Привет! Я Claude - ИИ-ассистент, созданный компанией Anthropic. Я стараюсь быть полезным и вести этичные беседы. Как я могу помочь вам сегодня?'}], 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 68}}