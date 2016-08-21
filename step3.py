import requests

#grab needle and haystack

token = {'token':'36195bfa379afc49b9c42ab8ed2c25b9'}

req = requests.post("http://challenge.code2040.org/api/haystack", data=token)

resp = req.json()

needle = resp['needle']

haystack = resp['haystack']

#check for needle in haystack and grab index

index = -1

for x in range(len(haystack)):
	if needle == haystack[x]:
		index = x

#send index back to API

submit = {'token':token['token'],'needle':index}

val = requests.post("http://challenge.code2040.org/api/haystack/validate", data=submit)

print(val.text)
