import requests

subscription_key_1 = '597fb9372155489f8ff6b4180d29126b'
subscription_key_2 = 'eb9a7b9673c142bea7d4d2986f39aad5'

base_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/{}"

image_url = "https://pp.userapi.com/c841036/v841036647/6262e/SdY1giZbopU.jpg"

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": subscription_key_1
}

payload = {
    "url": image_url
}

params = {
    "returnFaceId": True,
    "returnFaceAttributes": "age,gender,smile,emotion,makeup"
}

request_url = base_url.format('detect')
r = requests.post(request_url, json=payload, headers=headers, params=params)

print(r)
data = r.json()
r_object = data[0]

print(r_object)

smile = r_object['faceAttributes']['smile']
gender = r_object['faceAttributes']['gender']

print(smile)
print(gender)
