import requests
import os
import json
import random

url = 'https://curiouscat.qa/api/v2/post/create'

questions = json.loads(open('StupidQuestions.json').read())
print("Json file loaded...")

username = input("Insert the username you want to spam here >> ")
nMessages = int(input("How many messages do you want to send >> "))

print("Spam started...")

for i in range(nMessages):
    question = questions[random.randint(0,91)]
    requests.post(url, allow_redirects=False, data = {
        'to': username,
        'anon': 'true',
        'question': question,
        'in_response_to': 'undefined',
        '_ob': 'registerOrSignin'
    })
    print(question)
    
print("Spam finished...")
    
