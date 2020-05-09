import requests
import os
import json

url = 'https://curiouscat.qa/api/v2/post/create'

questions = json.loads(open('StupidQuestions.json').read())
print("Json file loaded...")

username = input("Insert the username you want to spam here >> ")

print("Spam started...")

for question in questions:
    requests.post(url, allow_redirects=False, data = {
        'to': username,
        'anon': 'true',
        'question': question,
        'in_response_to': 'undefined',
        '_ob': 'registerOrSignin'
    })
    
print("Spam finished...")
    
