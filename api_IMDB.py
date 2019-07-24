import  requests #Here is your key: e48c2b4b
import json

def pesquisar_Filme(title):
    '''
    :Function: Faz um GET com a API pra receber as informações de um filme
    :param title: recebe um titulo de filme
    :return: As informações desse filme no formato JSON
    '''
    req = "http://www.omdbapi.com/?apikey=e48c2b4b&t="+title + "&type=movie"
    try:
        resp =  requests.get(req)
        return json.loads(resp.text)
    except Exception as e:
        print("ERRO:",  e)
        return None

def dados_Filme(filme):
    '''
    :param filme: informações desse filme no formato JSON
    :return: Não retorna nenhum valor, mas printa na tela algumas informações sobre o filme
    '''
    print("\n------------------------")
    if filme['Response'] == 'False':
        print("Filme não Encontrado!!!")
        print("------------------------")
        return
    print("Titulo do Filme:",filme['Title'])
    print("Data de Lancamento:",filme['Released'])
    print("Diretor:", filme['Director'])
    print("Nota IMdB:", filme['imdbRating'])
    print("Prêmios:",filme['Awards'])
    print("Poster:", filme['Poster'])

    print("------------------------")

while True:
    t = input("Informe o nome do Filme ou ENTER para sair:")
    if t == "\n":
        break
    else:
        dados_Filme(pesquisar_Filme(t))




