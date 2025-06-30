# pip install --upgrade requests
# pip install requests[socks]
import requests
from keys import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXY_HTTP, PROXY_SOCKS5H



path_file = None
#path_file = "./uploads/image45.png"

url = f"http://{HOST}/api/claude/"

data = {
    # Content-Type: application/x-www-form-urlencoded
    "access_id": ACCESS_ID,
    "user_content": "О, привет, ты снова тут",
    "system_content": "Ты девушка 27 лет",
    "model": "claude-3-haiku-20240307",
    #'assist_content': '[{"user": "Привет, меня зовут Алекс."}, {"assistant": "Очень приятно Алекс, я Ева."}, {"user": "Мне 40 лет."}, {"assistant": "Ты в самом расвете сил!"}]',
}

headers = {
    API_KEY: VALUE_KEY,
    "User-Agent": "Mozilla/5.0",
}

if path_file:
    with open(path_file, 'rb') as f:
        files = {
            # Content-Type: multipart/form-data
            'file': ('image.jpg', f),
            'access_id': (None, ACCESS_ID),
            'user_content': (None, "Как зовут актрису на рисунке?"),
            'model': (None, "gemini-2.0-flash")
        }
        response = requests.post(url, headers=headers, files=files, proxies=PROXY_SOCKS5H, timeout=200)
else:
    response = requests.post(url, headers=headers, data=data, proxies=PROXY_SOCKS5H, timeout=200)

print(response.status_code)
print(response.text)























#{'id': 'msg_015mwuobJH1K1X3tiZYdzEtu', 'type': 'message', 'role': 'assistant', 'model': 'claude-3-5-sonnet-20241022', 'content': [{'type': 'text', 'text': 'Привет! Я Claude - ИИ-ассистент, созданный компанией Anthropic. Я стараюсь быть полезным и вести этичные беседы. Как я могу помочь вам сегодня?'}], 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 68}}