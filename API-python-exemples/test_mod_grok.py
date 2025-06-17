import requests
from config import HOST, ACCESS_ID, API_KEY, VALUE_KEY, PROXIES

path_file = None
proxies = None

#path_file = "./uploads/image45.png"

url = f"http://{HOST}/api/grok/"


data = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded", 
    "access_id": ACCESS_ID,
    "user_content": "Привет",
    #'system_content': 'Ты личный асистент в Германии',
    "model": "grok-2-vision-latest",
    #'assist_content': '[{"user": "Привет, меня зовут Алекс."}, {"assistant": "Очень приятно Алекс, я Грок."}, {"user": "Мне 40 лет."}, {"assistant": "Ты в самом расвете сил!"}]',
}

headers = {
    API_KEY: VALUE_KEY,
}

if path_file:
    with open(path_file, 'rb') as f:
        file = {'file': ('image45.png', f)}
        response = requests.post(url, headers=headers, data=data, files=file, proxies=PROXIES, timeout=200)
else:
    response = requests.post(url, headers=headers, data=data, proxies=PROXIES, timeout=200)



if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)

# print(response)






# print(response)



#{'id': 'msg_015mwuobJH1K1X3tiZYdzEtu', 'type': 'message', 'role': 'assistant', 'model': 'claude-3-5-sonnet-20241022', 'content': [{'type': 'text', 'text': 'Привет! Я Claude - ИИ-ассистент, созданный компанией Anthropic. Я стараюсь быть полезным и вести этичные беседы. Как я могу помочь вам сегодня?'}], 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 68}}




# {'id': '5c301da4-d584-4296-8967-6f190f3fe3c3', 'object': 'chat.completion', 'created': 1739048859, 'model': 'grok-2-vision-1212', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': 'Привет', 'refusal': None}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 13, 'completion_tokens': 67, 'total_tokens': 80, 'prompt_tokens_details': {'text_tokens': 13, 'audio_tokens': 0, 'image_tokens': 0, 'cached_tokens': 0}}, 'system_fingerprint': 'fp_21e54090c4'}