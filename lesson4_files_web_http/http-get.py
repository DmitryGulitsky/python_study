import json
from pprint import pprint
import http.client

HOST = 'httpbin.org'
connection = http.client.HTTPConnection(HOST, port=80)
connection.request('GET', '/get')

response = connection.getresponse()
body = response.read().decode()
print('Response is:', body)

#body = response.read()
#print(body)

print('connection ', connection)
print('response ', response)
print('response.status ', response.status)
print('response.reason ', response.reason)
#print('body ', body)
#print('type(body) ', type(body))

# body = response.read().decode()
# print('body ', body)
# res = json.loads(body)
# equal
res = json.loads(response.read().decode())

pprint(res)

print('-----------------------------------')
print("pprint(res['headers'])")
pprint(res['headers'])

print('-----------------------------------')
# headers to string
print(repr(json.dumps(res['headers'])))

print('-----------------------------------')
print("type(json.dumps(res['headers']))")
print(type(json.dumps(res['headers'])))

