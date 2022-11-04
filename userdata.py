import requests
import json
data=requests.get("https://reqres.in/api/users?page=1").text
data_info=json.loads(data)
print(data_info)