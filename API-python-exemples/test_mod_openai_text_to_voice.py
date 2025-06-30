# pip install --upgrade requests
# pip install requests[socks]
import requests
from keys import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXY_HTTP, PROXY_SOCKS5H
import requests
import base64


url = f"http://{HOST}/api/openai-text-to-voice/"

data = {
    "access_id": ACCESS_ID,
    "user_content": "А ну-у-у-у-ка! Подика сюда, мальчик.)",
    "voice": "nova", # alloy, echo, fable, onyx, nova, and shimmer
    "model": "tts-1", # tts-1 or tts-1-hd
    "response_format": "wav", # mp3, opus, aac, flac, wav, and pcm
    "speed": 1.0, # 0.25 to 4.0
}

headers = {
    API_KEY: VALUE_KEY,
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, headers=headers, data=data, proxies=PROXY_SOCKS5H, timeout=200)

format_audio = data["response_format"]

if response.status_code == 200:
    # Получаем JSON-ответ
    json_response = response.json()
    b64_json = json_response.get("b64_json")

    if b64_json:
        # Декодируем строку Base64 обратно в бинарные данные
        audio_data = base64.b64decode(b64_json)

        # Сохраняем аудиофайл локально
        with open(f"./audio/output_audio.{format_audio}", "wb") as audio_file:
            audio_file.write(audio_data)

        print(f"The audio file is saved as output_audio.{format_audio}")

    elif isinstance(response, str):
        print(f"Error: {response}")

else:
    if isinstance(response, str):
        print(f"Error: {response}")
