import requests
from config import HOST, ACCESS_ID, API_KEY, VALUE_KEY

url = f"http://{HOST}/api/openai-voice-to-text/"

data = {
        "access_id": ACCESS_ID,
        "prompt": "переведи в текст",
        "language": "ru", # input language in ISO-639-1, will improve accuracy and latency - ru or en
        "model": "whisper-1", # whisper-1
        "response_format": "text", # json, text, srt, verbose_json, or vtt
        # timestamp_granularities=["word"],
        # timestamp_granularities=["segment"]
}

headers = {
    API_KEY: VALUE_KEY,
}

with open('./audio/in_audio_2.ogg', 'rb') as f:
    
    file = {
        'file': ('in_audio_2.ogg', f)
    }

    response = requests.post(url, headers=headers, data=data, files=file)

# Проверка статуса ответа и вывод результата
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)