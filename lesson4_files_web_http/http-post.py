import json
from pprint import pprint
import http.client

HOST = 'httpbin.org'
connection = http.client.HTTPConnection(HOST, port=80)

# data to POST
headers = {'Content-type': 'application/json'}
my_data = {
    'key': 'value',
    'spam': 'eggs',
    'what?': 42
}

request_body = json.dumps(my_data)
print('type(request_body) == ', type(request_body))

connection.request('POST', '/post', request_body, headers=headers)

response = connection.getresponse()
data = json.loads(response.read().decode())
pprint(data)
print("data['json'] == my_data", data['json'] == my_data)