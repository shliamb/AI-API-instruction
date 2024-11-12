import requests

image = None

url = "http://137.184.87.156:8000/api/claude/"

data = {
        'username': 'Shl4454', # !
        'user_content': 'Что ты видишь?', # !
        #'system_content': 'Тебя зовут Ева',
        'model': 'claude-3-haiku-20240307',
        #'assist_content': '[{"user": "Привет, меня зовут Алекс."}, {"assistant": "Очень приятно Алекс, я Ева."}, {"user": "Мне 40 лет."}, {"assistant": "Ты в самом расвете сил!"}]',
}

headers = {
    'appkey': '72d3d8e8-74c4-4ff6-9033-91e8670b3708',
}

with open('./uploads/image.jpg', 'rb') as file:
    image = {
        'image': ('image.jpg', file),  # !
    }

    response = requests.post(url, headers=headers, data=data, files=image)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)



#{'id': 'msg_015mwuobJH1K1X3tiZYdzEtu', 'type': 'message', 'role': 'assistant', 'model': 'claude-3-5-sonnet-20241022', 'content': [{'type': 'text', 'text': 'Привет! Я Claude - ИИ-ассистент, созданный компанией Anthropic. Я стараюсь быть полезным и вести этичные беседы. Как я могу помочь вам сегодня?'}], 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 68}}