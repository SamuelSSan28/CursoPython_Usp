import requests
import json

class Tradutor:

    def traduzir(texto):
        '''
        :Function: az um GET com a API para traduzir um texto
        :param texto: Recebe uma string em ingles
        :return: a tradução para o portugues do texto
        '''
        token = "trnsl.1.1.20190724T171344Z.cd8e86fef6926b21.48951608fcfcb34da8007c926af12e52b76eeab5"
        req = "https://translate.yandex.net/api/v1.5/tr.json/translate?key="+token+"&text="+texto+"&lang=en-pt"
        try:
            resp = requests.get(req)
            r =  json.loads(resp.text)
            return r['text'][0]
        except Exception as e:
            return "ERRO: "+ str(e)

