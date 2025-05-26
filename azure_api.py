import requests
from requests.auth import HTTPBasicAuth
from config import AZURE_ORG_URL, AZURE_PROJECT, AZURE_PAT

def get_work_items():
    query_url = f"{AZURE_ORG_URL}/{AZURE_PROJECT}/_apis/wit/wiql?api-version=6.0"
    wiql_query = {
        "query": """
            SELECT [System.Id], [System.Title]
            FROM WorkItems
            WHERE [System.AssignedTo] = @Me
            AND [System.State] IN ('New', 'Active', 'Resolved', 'Closed')
            AND [System.ChangedDate] >= @Today - 7
            AND [System.ChangedDate] <= @Today
            AND [System.WorkItemType] IN ('Epic', 'Task', 'Bug', 'User Story')
        """
    }

    try:
        response = requests.post(query_url, json=wiql_query, auth=HTTPBasicAuth('', AZURE_PAT))
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com Azure DevOps: {e}")
        return []

    if response.status_code != 200:
        print(f"Erro ao buscar work items: {response.status_code} - {response.text}")
        return []

    work_item_ids = [item["id"] for item in response.json()["workItems"]]

    if not work_item_ids:
        print("Nenhum item encontrado.")
        return []

    ids_str = ",".join(map(str, work_item_ids))
    details_url = f"{AZURE_ORG_URL}/{AZURE_PROJECT}/_apis/wit/workitems?ids={ids_str}&api-version=6.0"

    try:
        details_response = requests.get(details_url, auth=HTTPBasicAuth('', AZURE_PAT))
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes dos work items: {e}")
        return []

    if details_response.status_code == 200:
        return details_response.json().get("value", [])
    else:
        print(f"Erro ao buscar detalhes: {details_response.status_code} - {details_response.text}")
        return []
