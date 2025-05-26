import requests
from config import NOTION_TOKEN, NOTION_DATABASE_ID

notion_headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def criar_pagina(titulo, descricao=""):
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    {"text": {"content": titulo}}
                ]
            },
            "Descrição": {
                "rich_text": [
                    {"text": {"content": descricao}}
                ]
            }
        }
    }

    response = requests.post(url, headers=notion_headers, json=data)

    if response.status_code == 200:
        print(f"Tarefa '{titulo}' adicionada com sucesso!")
    else:
        print(f"Erro ao adicionar '{titulo}': {response.text}")