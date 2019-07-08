from pprint import pprint
import requests

headers = {
    'Content-type': 'application/json',
}

data = {
    'MySecretHeader': 'spam and eggs',
    'what?': 42
}

response = requests.post(
    'http://httpbin.org/post',
    headers=headers,
    json=data
)

response_json=response.json()

pprint(response)
pprint(response.text)
pprint(response.json())
pprint(response.json['json'] == data)