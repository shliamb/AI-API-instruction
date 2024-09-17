import requests

image = None

url = "http://137.184.87.156:8000/api/openai_chat/"

data = {
        "username": "Shliamb10",                                            # !
        "user_content": "Что на рисунке видишь?",                           # !
        # "system_content": "Ты крутой юморист, каждое слово - шутка",      #
        "model": "gpt-4o-mini-2024-07-18",                                  #
}

headers = {
    'appkey': '72d3d8e8-74c4-4ff6-9033-91e8670b3708',                       #
}

### comment to bypass the image
with open('./uploads/image.jpg', 'rb') as file:
    image = {
        'image': ('image.jpg', file),                                       #
    }
### comment to bypass the image

    response = requests.post(url, headers=headers, data=data, files=image)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)




# {'response': 'На рисунке изображена стилизованная маска головы собаки \
#  с острыми шипами. Маска выглядит зловеще и необычно, с изогнутыми линиями \
# и текстурой, создающей эффект глубины. Внизу находятся слова "MAD DOG AGONY", \
# что может указывать на название или тему, связанную с изображением. В целом, \
# композиция имеет тёмную и мрачную атмосферу.', 'expenses': 0.0766845, 'used_tokens': 51123}