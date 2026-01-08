import os
from dotenv import load_dotenv, find_dotenv
from helper import get_completion_from_messages

_ = load_dotenv(find_dotenv())

api_key = os.environ["OPENAI_API_KEY"]
print("OpenAI API lida com sucesso!")

messages =  [  
{'role':'system', 'content':'Você é um chatbot amigável.'},
{'role':'user', 'content':'Olá, meu nome é Maria'},
{'role':'assistant', 'content': "Olá Maria! Prazer em conhecê-la. \
Há algo em que eu possa ajudá-lo hoje?"},
{'role':'user', 'content':'Sim, você poderia me recordar, Qual é o meu nome?'}  ]

response = get_completion_from_messages(api_key, messages, temperature=1)
print(response)
