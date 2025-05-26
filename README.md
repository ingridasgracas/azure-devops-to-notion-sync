# Azure DevOps to Notion Sync

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Notion API](https://img.shields.io/badge/Notion-API-black?logo=notion&logoColor=white)](https://developers.notion.com/)
[![Azure DevOps](https://img.shields.io/badge/Azure_DevOps-API-blue?logo=azure-devops&logoColor=white)](https://learn.microsoft.com/en-us/rest/api/azure/devops/)

Script em Python para sincronizar tarefas do **Azure DevOps** com uma database personalizada no **Notion**.

## ✨ Funcionalidades

- 🔍 Lê e filtra work items do Azure DevOps via API
- 🧱 Cria uma página no Notion para cada tarefa automaticamente
- 📋 Mapeia os campos essenciais: título, estado, responsável, descrição e outros
- 📦 Estrutura modular com separação de configs, requisições e lógica principal

## 🚧 Funcionalidades futuras

- 🔁 Atualizar páginas existentes no Notion (não duplicar tarefas)
- ⏰ Agendamento automático com cron jobs
- 🔔 Integração via webhook para sincronização em tempo real
- 📊 Mapeamento bidirecional (Notion → Azure DevOps)

## 🛠️ Pré-requisitos

- Python 3.8 ou superior
- Conta no [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/)
- Conta no [Notion](https://www.notion.so/) com a API ativada
- Criar uma integração no Notion e compartilhar com sua database

