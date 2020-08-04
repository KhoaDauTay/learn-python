import requests, json

base_url1 = "http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh"
base_url2 = "http://worldtimeapi.org/api/timezone/Asia/Hong_Kong"
base_url3 = "http://worldtimeapi.org/api/timezone/America/New_York"
base_url4 = "http://worldtimeapi.org/api/timezone/Asia/Tokyo"
base_url5 = "http://worldtimeapi.org/api/timezone/Europe/London"

response1 = requests.get(base_url1)
x1 = response1.json()
print(x1["timezone"])
print(x1["utc_datetime"])

response2 = requests.get(base_url2)
x2 = response2.json()
print(x2["timezone"])
print(x2["utc_datetime"])

response3 = requests.get(base_url3)
x3 = response3.json()
print(x2["timezone"])
print(x2["utc_datetime"])

response4 = requests.get(base_url4)
x4 = response4.json()
print(x4["timezone"])
print(x4["utc_datetime"])

response5 = requests.get(base_url5)
x5 = response5.json()
print(x5["timezone"])
print(x5["utc_datetime"])






