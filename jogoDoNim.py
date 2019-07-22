def mostraJogada(u,n,m):
    if u == "m":
        if m == 1:
            print("\nO computador tirou uma peça.")
        else:
            print("\nO computador tirou",m,"peças.")
    else:
        if m == 1:
            print("\nVocê tirou uma peça.")
        else:
            print("\nVoce tirou",m,"peças.")

    if n - m > 1 :
        print("Agora restam", (n - m), "peças no tabuleiro.")
    elif n - m == 1:
        print("Agora resta apenas uma peça no tabuleiro.")

def computador_escolhe_jogada(n,m):
    N = n
    while n%(m+1) == 0 or n > m:
        n -= 1

    if n == 0:
        mostraJogada("m",n,m)
        return m

    mostraJogada("m", N, n)
    return n

def usuario_escolhe_jogada(n,m):
    nU = int(input("\nQuantas peças você vai tirar?"))
    while nU > m or nU < 0:
        print("\nOops! Jogada inválida! Tente de novo.")
        nU = int(input("\nQuantas peças você vai tirar?"))

    mostraJogada("u",n,nU)
    return nU


def partida():
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n%(m+1) != 0:
        print("\nComputador começa!")
        while n > 0:
            n -= computador_escolhe_jogada(n,m)
            if n == 0:
                print("\nFim do jogo! O computador ganhou!")
                return 0
            n -= usuario_escolhe_jogada(n,m)
            if n == 0:
                print("\nFim do jogo! Você ganhou!")
                return 1
    else:
        print("\nVoce começa!")
        while n > 0:
            n -= usuario_escolhe_jogada(n,m)
            if n == 0:
                print("\nFim do jogo! Você ganhou!")
                return 1
            n -= computador_escolhe_jogada(n,m)
            if n == 0:
                print("\nFim do jogo! O computador ganhou!")
                return 0


def campeonato():
    pU = 0
    pM = 0
    i =1
    while i <= 3:
        print("**** Rodada",i,"****")
        if partida() == 1:
            pU += 1
        else:
            pM += 1
        i +=1
        print("**** Fim da Rodada",i,"****")

    print("\n**** Final do campeonato! ****")
    print("\nPlacar:",pU,"X",pM," Computador")



def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    op  = int(input())
    if op == 1:
        print("Voce escolheu uma partida!")
        partida()
    elif op == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
    else:
        print("Opção Invalida!!")


main()