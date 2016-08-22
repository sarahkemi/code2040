import requests
import json

#obtain the prefix and the array!!

token = {'token':'36195bfa379afc49b9c42ab8ed2c25b9'}

req = requests.post("http://challenge.code2040.org/api/prefix", data=token)

resp = req.json()

prefix = resp['prefix']

array = resp['array']

#check every string in array for prefix! append strings that don't start with prefix to new array

no_prefix = []

for string in array:
	if not string.startswith(prefix):
		no_prefix.append(string)

#send new array back to API

submit = json.dumps({'token':token['token'], 'array':no_prefix})

headers = {'Content-Type': 'application/json'}

#here, it turned out that it was super important that I sent the array back to the API with a json dump and headers!!
#I didn't have to do this for the other steps because I was only POSTing text or integers

val = requests.post("http://challenge.code2040.org/api/prefix/validate", data=submit, headers=headers)

print(val.text)
