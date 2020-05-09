import requests
import os
import json
import random

url = 'https://curiouscat.qa/api/v2/post/create'

questions = json.loads(open('StupidQuestions.json').read)

for quetion in questions:
    request.post(url, allow_redirects=False, data = {
        'to': '' #Insert username here
        'anon': 'true'
        'question': question
        'in_response_to': 'undefined'
        '_ob': 'registerOrSignin'
    })
    
