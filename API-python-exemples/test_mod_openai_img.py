import requests
from config import HOST, ACCESS_ID, API_KEY, VALUE_KEY

url = f"http://{HOST}/api/openai-img/"

data = {
        "access_id": ACCESS_ID,
        "user_content": "логотип для телеграмм бота, по середине написанно API, в круге, в технологическом стиле, буд то пронизано все проводниками, микросхемы.", # !
        #"quality": "standard", # standard or hd
        "style": "vivid", # vivid ore natural
        #"size": "1024x1024", 
        #"response_format": "url",
        #"n": 1,
        #"model": "dall-e-2"

}

headers = {
    API_KEY: VALUE_KEY,
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)
