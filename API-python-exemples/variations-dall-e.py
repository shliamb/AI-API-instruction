import requests

files = None

url = "http://137.184.87.156:8000/api/variations-dall-e/"

data = {
        "username": "Shliamb10",                                # !
        "size": "1024x1024",                                    # 
        "response_format": "url",                               #
        "n": 1,                                                 #
        "model": "dall-e-2"                                     # 

}

headers = {
    'appkey': '72d3d8e8-74c4-4ff6-9033-91e8670b3708',           # !
}

with open('./uploads/image45.png', 'rb') as image:

    files = {
        'file': ('image45.png', image),                         # !
    }

    response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)



# 