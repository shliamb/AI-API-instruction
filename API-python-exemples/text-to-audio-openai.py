import requests
import base64

url = "http://137.184.87.156:8000/api/speech-to-audio-openai/"

data = {
        "username": "Shliamb10",                                            # !                                     
        "user_content": "А ну-у-у-у-ка! Подика сюда, мальчик...",           # !
        "voice": "nova", # alloy, echo, fable, onyx, nova, and shimmer      #
        "model": "tts-1-hd", # tts-1 or tts-1-hd                            #
        "response_format": "wav", # mp3, opus, aac, flac, wav, and pcm      #
        "speed": 1.0, # 0.25 to 4.0                                         #
}

headers = {
    'appkey': '72d3d8e8-74c4-4ff6-9033-91e8670b3708',                       # !
}

response = requests.post(url, headers=headers, data=data)

format_audio = data["response_format"]

if response.status_code == 200:

    json_response = response.json()
    b64_json = json_response.get("b64_json")

    if b64_json:
        audio_data = base64.b64decode(b64_json)

        with open(f"./audio/output_audio.{format_audio}", "wb") as audio_file:
            audio_file.write(audio_data)

        print(f"The audio file is saved as output_audio.{format_audio}")
else:
    print(f"Error: {response.status_code} - {response.text}")


# Only file