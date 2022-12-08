import requests
import json

url = "https://webexapis.com/v1/messages"

payload = json.dumps({
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vY2ExMjM3ZDAtZmM0NC0xMWVjLWJjM2ItNDE4M2VkM2ZiODQ4",
  "text": "Huhu CCWN"
})
headers = {
  'Authorization': 'Bearer NDZjZTFjMmQtZjI4Yi00ZjRjLTkwM2QtMDQ5MzYwZjY1MWUzNTZmYWY2MmItMWM2_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605',
  'Content-Type': 'application/json'
}


for i in (range(1,100000,1)):
    response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
