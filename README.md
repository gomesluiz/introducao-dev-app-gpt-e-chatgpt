# Introdução ao Desenvolvimento de Apps com GPT e ChatGPT

Este repositório reúne os exemplos de código do [ICEITalks](https://youtu.be/iI0OsJIomXo), evento realizado em 23 de novembro de 2023. O material apresenta conceitos de GPT e ChatGPT e demonstra o uso de APIs em aplicações práticas.

## Requisitos

- Python 3
- Uma chave de API da OpenAI

## Instalação

Na raiz do repositório, crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Instale os pacotes Python listados em `requirements.txt`:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configuração da chave de API

Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

```dotenv
OPENAI_API_KEY=sua_chave_de_api
```

O arquivo `.env` está no `.gitignore`; não compartilhe nem publique sua chave.

## Executar os exemplos

Com o ambiente virtual ativado e a chave configurada, execute um script a partir da raiz do repositório:

```bash
python basico_1.py
python chatbot_1.py
python chatbot_2.py
python classificacao_1.py
```

`chatbot_2.py` inicia uma conversa interativa; envie uma mensagem vazia para encerrar. O arquivo `helper.py` contém uma função compartilhada pelos exemplos e não precisa ser executado diretamente.
