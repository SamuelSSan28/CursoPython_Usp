import requests
import json
from translator import Tradutor

def clima(cidade):
    '''
    :Function: Faz um GET com a API pra receber as informações de uma cidade
    :param cidade: Recebe o nome da cidade
    :return: Retorna uma lista cotendo o clima e a temperatura(°K) desta cidade
    '''
    token = "ce69bcad70f6ca8411463ecd0e2fb7b3"
    req = " https://api.openweathermap.org/data/2.5/weather?q="+cidade+",br&APPID="+token
    try:
        resp = requests.get(req)
        print(resp)
        r =  json.loads(resp.text)
        return [r['weather'][0]['main'],r['main']['temp']]
    except Exception as e:
        print("ERRO:", e)
        return None




city = input("Informe o nome da sua Cidade: ")

c = clima(city)
if c:
    c[1] = float(c[1]) - 273.15
    print("Condição Climatica: ",Tradutor.traduzir(c[0]))
    print("Temperatura: {0:.2f} °C".format(c[1]))
else:
    print("Nada")