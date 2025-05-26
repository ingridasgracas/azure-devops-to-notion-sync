import requests
from requests.auth import HTTPBasicAuth

url = url = ""
token = ""


response = requests.get(url, auth=HTTPBasicAuth('', token))

print(response.status_code)
print(response.text)
