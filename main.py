from azure_api import get_work_items
from notion_api import criar_pagina

def main():
    work_items = get_work_items()

    for item in work_items:
        titulo = f"Tarefa #{item['id']}"
        descricao = item.get('fields', {}).get('System.Title', 'Sem descrição')

        criar_pagina(titulo, descricao)

if __name__ == "__main__":
    main()
    