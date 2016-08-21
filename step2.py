import requests

#grab string from API

token = {'token':'36195bfa379afc49b9c42ab8ed2c25b9'}

req = requests.post("http://challenge.code2040.org/api/reverse", data=token)

string = req.text

#send reversed string back to validate

data = {'token':token['token'], 'string':string[::-1]}

val = requests.post("http://challenge.code2040.org/api/reverse/validate", data=data)

print(val.text)