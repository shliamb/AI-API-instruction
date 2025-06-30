# pip install --upgrade requests
# pip install requests[socks]
import requests
from keys import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXY_HTTP, PROXY_SOCKS5H

url = f"http://{HOST}/api/openai-voice-to-text/"

headers = {
    API_KEY: VALUE_KEY,
    "User-Agent": "Mozilla/5.0"
}

with open('./audio/in_audio.ogg', 'rb') as f:
    
    files = {
        'file': ('in_audio.ogg', f),
        'access_id': (None, ACCESS_ID),
        'prompt': (None, "переведи в текст"),
        'model': (None, "whisper-1"),
        'response_format': (None, "text")
    }

    response = requests.post(url, headers=headers, proxies=PROXY_SOCKS5H, files=files, timeout=200)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)








# file = {
#         "access_id": ACCESS_ID,
#         "prompt": "переведи в текст",
#         #"language": "ru", # input language in ISO-639-1, will improve accuracy and latency - ru or en
#         "model": "whisper-1", # whisper-1
#         "response_format": "text", # json, text, srt, verbose_json, or vtt
#         # timestamp_granularities=["word"],
#         # timestamp_granularities=["segment"]
# }
