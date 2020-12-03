import json
import requests

req = requests.get('http://127.0.0.1:8000/chain')

# Page encoding
e = req.encoding
print("Encoding: ",e)

# Response code
s = req.status_code
print("Response code: ",s)

# Response Time
t = req.elapsed
print("Response Time: ",t)


t = req.headers['Content-Type']
print("Header: ",t)

z = req.text
#print("\nSome text from the web page:\n",z)#[0:1000])
parsed = json.loads(z)
print (json.dumps(parsed, indent=2, sort_keys=True))