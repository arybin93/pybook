import requests

URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/{}'

key1 = '597fb9372155489f8ff6b4180d29126b'
key2 = 'eb9a7b9673c142bea7d4d2986f39aad5'

detect_url = URL.format('detect')

file = {
    'url': 'https://www.rusdialog.ru/images/news/a1461f7e259fc936e342d67f40633a17.jpg'
}

params = {
    'returnFaceId': True,
    'returnFaceAttributes': 'age,emotion'
}

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key1
}

print(detect_url)

r = requests.post(detect_url, params=params, headers=headers, json=file)

print(r.status_code)
print(r.text)
