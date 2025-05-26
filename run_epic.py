import requests

token = '363p82D7ClfhKBAKeoSsipwPTLN40j0smFuMg5ZomVcoOW55XrAuJQQJ99BEACAAAAAsfoTXAAASAZDO3uGg'  # Cola seu Internal Integration Token aqui
database_id = 's1f43e91158cb80e484adc0cc2f1de97b'  # Cola seu Database ID aqui (sem traços)

url = f'https://api.notion.com/v1/databases/{database_id}/query'
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",  # Pode atualizar a versão se quiser
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
data = response.json()

# Vamos imprimir os títulos das epics
for page in data.get('results', []):
    props = page['properties']
    # Supondo que o título está numa propriedade chamada 'Name' ou similar
    title_prop = props.get('Title', {})
    if title_prop.get('type') == 'Title':
        title = ''.join([t['plain_text'] for t in title_prop['Title']])
        print(Title)
