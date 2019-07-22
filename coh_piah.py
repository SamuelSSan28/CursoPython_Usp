import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    simi = 0
    for i in range(6):
        simi += max(as_a[i],as_b[i]) - min(as_b[i],as_a[i])

    return simi/6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = []
    sentencas = separa_sentencas(texto) #separa as sentencas do texto

    frases = []
    somaS = 0
    for s in sentencas:
        frases += separa_frases(s) #separa as frases das sentençascont = 0
        somaS += len(s)
    palavras = []
    somaF = 0
    for f in frases:
        palavras += separa_palavras(f) #separa as palavras de todas frases
        cont = 0
        for c in f:
            if c == ',' or c == ';' or c == '.' or c == '\n':
                cont += 1
        somaF += len(f) - cont

    soma = 0
    for p in palavras:
        if p ==',' or  p ==';'  or  p =='.' or  p =='\n':
            continue
        soma += len(p)

    #Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    tam_medio_pal = soma/len(palavras)

    #Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    type_token = n_palavras_diferentes(palavras)/len(palavras)

    #Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
    hapax_legomana = n_palavras_unicas(palavras)/len(palavras)

    #Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    complexidade = len(frases)/len(sentencas)

    #Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
    tam_medio_sent = somaS/len(sentencas)

    #Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
    tam_medio_frase = somaF/len(frases)

    return [tam_medio_pal,type_token,hapax_legomana,tam_medio_sent,complexidade,tam_medio_frase]


def avalia_textos(textos, ass_cp):
    ''' Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    listaSimilaridade = []
    for i in textos:
        ass_i = calcula_assinatura(i)  # para cada texto calcula a assinatura
        listaSimilaridade.append(compara_assinatura(ass_i, ass_cp))  # para cada texto, compara
        # a sua ass com a ass da pessoa com COH-PIAH

    return listaSimilaridade.index(min(listaSimilaridade)) + 1


def main():
    infectado = le_assinatura()
    textos = le_textos()
     #pega o texto com a menor similaridade
    t = avalia_textos(textos,infectado)
    print("O autor do texto", t, "está infectado com COH-PIAH")




def test_1():
    textos = [
        "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.",
        "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
        "Navegadores antigos tinham uma frase gloriosa:'Navegar é preciso; viver não é preciso'. Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
    ]
    infectado = [4.79,0.72,0.56,80.5,2.5,31.6]
    listaASS = []
    for i in textos:
        ass_i = calcula_assinatura(i)
        listaASS.append(ass_i)

    print(listaASS[2])
    assert  listaASS[0]  == [5.1891891891891895, 0.7432432432432432, 0.6081081081081081, 466.0, 10.0, 45.7]
    assert  listaASS[1]  == [4.507936507936508, 0.7777777777777778, 0.6666666666666666, 88.875, 3.25, 26.653846153846153]
    assert  listaASS[2]  == [4.409448818897638, 0.5905511811023622, 0.36220472440944884, 86.125, 2.0, 42.5625]

def test_2():
    textos = [
        "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.",
        "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
        "Navegadores antigos tinham uma frase gloriosa:'Navegar é preciso; viver não é preciso'. Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
        ]
    infectado = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    listaSimilaridade = []
    for i in textos:
        ass_i = calcula_assinatura(i)
        listaSimilaridade.append(compara_assinatura(ass_i,infectado))

    t = listaSimilaridade.index(min(listaSimilaridade)) + 1
    print("O autor do texto", t, "está infectado com COH-PIAH")
    assert  listaSimilaridade == [67.92842342342342, 2.4196102971102973, 2.9658825459317586]


main()