import requests
import json

def cotacao_moeda(moeda):
    '''
    :Function: az um GET com a API pra receber as informações de uma moeda
    :param moeda: Recebe um tipo de moeda ["USD","EUR","BTC",...]
    :return: uma lista com valores da moeda ["em alta"."em baixa"]
    '''
    req = "https://economia.awesomeapi.com.br/all/"+moeda+"-BRL"
    try:
        resp = requests.get(req)
        r =  json.loads(resp.text)
        return [r[moeda]['high'],r[moeda]['low']]
    except Exception as e:
        print("ERRO:", e)
        return None



moedas = ["USD","EUR","BTC"]
print("Escolha uma moeda:",moedas)
m = input()
c = cotacao_moeda(m)

if c:
    print("Valor em alta:",c[0],"\nValor em baixa:",c[1])