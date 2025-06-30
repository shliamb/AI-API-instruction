# pip install --upgrade requests
# pip install requests[socks]
import requests
from keys import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXY_HTTP, PROXY_SOCKS5H


path_file = None
path_file = "./uploads/image45.png"

url = f"http://{HOST}/api/openai-chat/"

data = {
    # Content-Type: application/x-www-form-urlencoded
    "access_id": ACCESS_ID,
    "user_content": "О, привет, ты снова тут",
    "system_content": "Ты девушка 27 лет",
    "model": "gpt-4o-mini-2024-07-18",
    # "assist_content": '[{"user": "How do I charge my battery?"}, {"assistant": "You should use the provided charging cable."}, {"user": "But it doesn\'t seem to charge."}, {"assistant": "Try another charge.."}]',
    # 'response_format': '{"type":"json_schema","json_schema":{"name":"user_profile","schema":{"type":"object","properties":{"name":{"description":"The name of the user","type":"string"},"age":{"description":"The age of the user","type":"integer"},"interests":{"description":"List of users interests","type":"array","items":{"type":"string"}}},"required":["name","age","interests"]}}}',
    # 'response_format': '{"type": "json_object"}' # if not,  response_format is {"type": "text"}
}

headers = {
    API_KEY: VALUE_KEY,
    "User-Agent": "Mozilla/5.0"
}

if path_file:
    with open(path_file, 'rb') as f:
        files = {
            # Content-Type: multipart/form-data
            "file": ('image.jpg', f),
            'access_id': (None, ACCESS_ID),
            'user_content': (None, "Как называется прическа девушки на рисунке, приблезительно?"),
            'model': (None, "gpt-4o-mini-2024-07-18")
        }
        response = requests.post(url, headers=headers, data=data, proxies=PROXY_SOCKS5H, files=files, timeout=200)
else:
    response = requests.post(url, headers=headers, data=data, proxies=PROXY_SOCKS5H, timeout=200)

print(response.status_code)
print(response.text)

