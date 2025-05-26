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

# Vamos imprimir os títulos das epics
for page in data.get('results', []):
    props = page['properties']
    title_prop = props.get('Title', {})
    if title_prop.get('type') == 'Title':
        title = ''.join([t['plain_text'] for t in title_prop['Title']])
        print(Title)
