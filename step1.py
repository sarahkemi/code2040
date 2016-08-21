import requests

#registration data

data = {'token':'36195bfa379afc49b9c42ab8ed2c25b9','github':'https://github.com/sarahkemi/code2040'}

reg = requests.post("http://challenge.code2040.org/api/register", data=data)

print(reg.text)