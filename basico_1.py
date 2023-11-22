import os
from dotenv import load_dotenv, find_dotenv
from helper import get_completion_from_messages

_ = load_dotenv(find_dotenv())

api_key = os.environ["OPENAI_API_KEY"]
print("OpenAI API lida com sucesso!")

mensagens = [{"role": "user", "content": "Quem descobriu o Brasil?"}]
respostas = get_completion_from_messages(api_key, mensagens)
print(respostas)
