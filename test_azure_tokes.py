import requests
from requests.auth import HTTPBasicAuth

url = url = "https://dev.azure.com/tjerj/_apis/projects?api-version=6.0"
token = "363p82D7ClfhKBAKeoSsipwPTLN40j0smFuMg5ZomVcoOW55XrAuJQQJ99BEACAAAAAsfoTXAAASAZDO3uGg"


response = requests.get(url, auth=HTTPBasicAuth('', token))

print(response.status_code)
print(response.text)
