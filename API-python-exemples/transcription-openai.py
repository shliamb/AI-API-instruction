import requests

url = "http://137.184.87.156:8000/api/transcription-openai/"

data = {
        "username": "Shliamb10",                                                                        # !
        "prompt": "переведи в текст",                                                                   # 
        "language": "ru", # input language in ISO-639-1, will improve accuracy and latency - ru or en   #
        "model": "whisper-1", # whisper-1                                                               #
        "response_format": "text", # json, text, srt, verbose_json, or vtt                              #
        # timestamp_granularities=["word"],                                                             # Not suport
        # timestamp_granularities=["segment"]                                                           # Not suport
}

headers = {
    'appkey': '72d3d8e8-74c4-4ff6-9033-91e8670b3708',                                                   # !
}

with open('./audio/in_audio_2.ogg', 'rb') as f:
    
    file = {
        'audio': ('in_audio_2.ogg', f)                                                                  # !
    }

    response = requests.post(url, headers=headers, data=data, files=file)

# Проверка статуса ответа и вывод результата
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)



#




