import requests

token = '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'
database_id = '1ff3e91158cb80f9a221efaaa2ac5666'

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
