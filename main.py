# aqui vai ficar a vericação dos estados de jogo
# as chamadas das funções
# e a chamada da classe jogo
import mao
import peca
import funcoes
import tabuleiro
import os

while True:
    domino = funcoes.criar_domino()
    domino = funcoes.embaralhar_domino(domino)
    print(domino)
    QNTD_JOGADORES = int(input('Quantos jogadores? '))
    while QNTD_JOGADORES < 2 or QNTD_JOGADORES > 4:
        os.system('clear')
        print('Número de jogadores inválido')
        QNTD_JOGADORES = int(input('Quantos jogadores? '))
    if QNTD_JOGADORES == 4:
        mao1 = funcoes.criar_mao(domino)
        mao2 = funcoes.criar_mao(domino)
        mao3 = funcoes.criar_mao(domino)
        mao4 = funcoes.criar_mao(domino)

        print("Jogador 1:")
        mao.mao_jogador.mostrar_mao(mao1)
        print("Jogador 2:")
        mao.mao_jogador.mostrar_mao(mao2)
        print("Jogador 3:")
        mao.mao_jogador.mostrar_mao(mao3)
        print("Jogador 4:")
        mao.mao_jogador.mostrar_mao(mao4)

    elif QNTD_JOGADORES == 3:
        mao1 = funcoes.criar_mao(domino)
        mao2 = funcoes.criar_mao(domino)
        mao3 = funcoes.criar_mao(domino)

        print("Jogador 1:")
        mao.mao_jogador.mostrar_mao(mao1)
        print("Jogador 2:")
        mao.mao_jogador.mostrar_mao(mao2)
        print("Jogador 3:")
        mao.mao_jogador.mostrar_mao(mao3)

    elif QNTD_JOGADORES == 2:
        mao1 = funcoes.criar_mao(domino)
        mao2 = funcoes.criar_mao(domino)

        print("Jogador 1:")
        mao.mao_jogador.mostrar_mao(mao1)
        print("Jogador 2:")
        mao.mao_jogador.mostrar_mao(mao2)