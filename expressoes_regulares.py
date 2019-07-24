import re
import requests

resp =  requests.get("https://portal.ifma.edu.br/contatos/")

teste = "samuel_22@gmail.com, ana@hotmail.com, jaoao@outlook.com"

padrao = re.search(r'[\w+\-]+@\w+\.\w+',resp.text) # primeira ocorrencia
padraoAll = re.findall(r'\w+@\w+\.\w+',resp.text) # todas as ocorrencias

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado")

if padraoAll:
    print(padraoAll)
else:
    print("Padrão não encontrado")