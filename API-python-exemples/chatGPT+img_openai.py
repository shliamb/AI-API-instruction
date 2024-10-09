import requests

image = None

url = "http://137.184.87.156:8000/api/openai_chat/"

data = {
        "username": "Shliamb10",                                            # !
        "user_content": "Что на рисунке видишь?",                           # !
        "system_content": "Ты личный асистент",                             #
        "model": "gpt-4o-mini-2024-07-18",                                  #
        'assist_content': '[{"user": "How do I charge my battery?"}, {"assistant": "You should use the provided charging cable."}, {"user": "But it doesn\'t seem to charge."}, {"assistant": "Try another charge.."}]',
        'response_format': '{"type": "text"}'                               # {"type": "text"}, {"type": "json_object"}, json_schema
        #'response_format': '{"type":"json_schema","json_schema":{"name":"user_profile","schema":{"type":"object","properties":{"name":{"description":"The name of the user","type":"string"},"age":{"description":"The age of the user","type":"integer"},"interests":{"description":"List of users interests","type":"array","items":{"type":"string"}}},"required":["name","age","interests"]}}}',

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