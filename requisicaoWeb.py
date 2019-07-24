import  requests

try:
    requisicao = requests.get("https://g1.globo.com/ma/maranhao/")
    print(requisicao.text)
except Exception as e:
    print("ERRO:",e)