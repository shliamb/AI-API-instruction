import requests

image = None

url = "http://137.184.87.156:8000/api/edit-dall-e/"

data = {
        "username": "Shliamb10",                                    # !
        #"size": "1024x1024",                                       #
        "user_content": "Дорисуй"                                   # !
        #"response_format": "url",                                  #
        #"n": 2,                                                    #
        #"model": "dall-e-2"                                        #
}

headers = {
    'appkey': '72d3d8e8-74c4-4ff6-9033-91e8670b3708',               #
}

### comment to bypass the image
with open('./uploads/edit.png', 'rb') as edit_file:#, \             # !
     #open('./uploads/lips.png', 'rb') as lips_file:                #
    
    image = {
        'image': ('edit.png', edit_file),                           # !
       # 'mask': ('lips.png', lips_file),                           # 
    }
### comment to bypass the image

    response = requests.post(url, headers=headers, data=data, files=image)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code, response.text)



# put url link