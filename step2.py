import requests

#grab string from API

token = {'token':'c9f5cfe5b9bb943bd587baed3e3d99c3'}

req = requests.post("http://challenge.code2040.org/api/reverse", data=token)

string = req.text

#send reversed string back to validate

data = {'token':token['token'], 'string':string[::-1]}

val = requests.post("http://challenge.code2040.org/api/reverse/validate", data=data)

print(val.text)