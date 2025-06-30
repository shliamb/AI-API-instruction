# pip install --upgrade requests
# pip install requests[socks]
import requests
from keys import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXY_HTTP, PROXY_SOCKS5H




path_file = None
#path_file = "./uploads/image45.png"

url = f"http://{HOST}/api/grok/"

data = {
    # Content-Type: application/x-www-form-urlencoded
    "access_id": ACCESS_ID,
    "user_content": "О, привет, ты снова тут",
    "system_content": "Ты девушка 27 лет",
    "model": "grok-2-vision-latest",
    #'assist_content': '[{"user": "Привет, меня зовут Алекс."}, {"assistant": "Очень приятно Алекс, я Грок."}, {"user": "Мне 40 лет."}, {"assistant": "Ты в самом расвете сил!"}]',
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

