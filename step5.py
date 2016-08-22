import requests
import datetime as dt

#get the necessary datestamp and interval

token = {'token':'36195bfa379afc49b9c42ab8ed2c25b9'}

req = requests.post("http://challenge.code2040.org/api/dating", data=token)

resp = req.json()

datestamp = resp['datestamp']

interval = resp['interval']

#convert the datestamp and interval into datetime objects, then add them

dt_datestamp = dt.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")

dt_interval = dt.timedelta(seconds=interval)

new_time = (dt_datestamp + dt_interval).strftime("%Y-%m-%dT%H:%M:%SZ") #need to convert back to ISO 8601

#send new time back to API

submit = {'token':token['token'], 'datestamp':new_time}

val = requests.post("http://challenge.code2040.org/api/dating/validate", data=submit)

print(val.text)
