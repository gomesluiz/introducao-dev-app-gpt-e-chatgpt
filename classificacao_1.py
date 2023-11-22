import os
from dotenv import load_dotenv, find_dotenv
from helper import get_completion_from_messages

_ = load_dotenv(find_dotenv())

api_key = os.environ["OPENAI_API_KEY"]
print("OpenAI API lida com sucesso!")

delimiter = "####"
system_message = f"""
Você receberá perguntas de atendimento ao aluno. \
A consulta de atendimento ao aluno será delimitada com \
os caracteres {delimiter}.
Classifique cada consulta em uma categoria primária \
e em uma secundária. 
Forneça a sua saída no formato JSON com as \
chaves: primaria and secundaria.

Categorias primárias: Financeiro, Suporte Técnico, \
Acadêmico, ou Geral.

Categorias secundárias do Financeiro:
Emissão de segunda via do boleto
Descontos na mensalidade

Categorias secundárias do Suporte Técnico:
Redefinição da senha da rede
Acesso a wifi da universidade

Categorias secundárias do Acadêmico:
Registro de abono de faltas
Matrícula em disciplina 

Categorias secundárias do Geral:
Informação sobre vestibular
Falar com um humano

"""
user_message = f"""\
Eu quero imprimir a segunda via do boleto para pagamento em atraso"""
messages =  [  
{'role':'system', 
 'content': system_message},    
{'role':'user', 
 'content': f"{delimiter}{user_message}{delimiter}"},  
] 
response = get_completion_from_messages(api_key, messages)
print(response)
