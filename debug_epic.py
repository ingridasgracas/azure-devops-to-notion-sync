import requests

token = ''
database_id = ''

url = f'https://api.notion.com/v1/databases/{database_id}/query'
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
data = response.json()

print("Resposta completa da API:")
print(data)
