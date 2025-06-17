import requests
from config import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXIES

path_file = None
proxies = None

# path_file = "./uploads/image.jpg"

url = f"http://{HOST}/api/openai-chat/"

data = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",  # или multipart/form-data (если файл)
    "access_id": ACCESS_ID,
    "user_content": "Ты сегодня не добрая)",
    "system_content": "Ты девушка 27 лет",
    "model": "gpt-4o-mini-2024-07-18",
}

headers = {
    API_KEY: VALUE_KEY,
}

if path_file:
    with open(path_file, 'rb') as f:
        file = {'file': ('image.jpg', f)}
        response = requests.post(url, headers=headers, data=data, proxies=PROXIES, files=file, timeout=200)
else:
    response = requests.post(url, headers=headers, data=data, proxies=PROXIES, timeout=200)



if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)




