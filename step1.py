import requests

#registration data

data = {'token':'c9f5cfe5b9bb943bd587baed3e3d99c3','github':'https://github.com/sarahkemi/code2040'}

reg = requests.post("http://challenge.code2040.org/api/register", data=data)

print(reg.text)