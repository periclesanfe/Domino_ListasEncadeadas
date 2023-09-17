# aqui vai ficar a vericação dos estados de jogo
# as chamadas das funções
# e a chamada da classe jogo
from mao import mao_jogador
from peca import peca
import funcoes as func
from tabuleiro import tabuleiro
import os

while True:
    domino = func.criar_domino()
    domino = func.embaralhar_domino(domino)
    func.mostrar_domino(domino)
    QNTD_JOGADORES = int(input('Quantos jogadores: '))
    while QNTD_JOGADORES < 2 or QNTD_JOGADORES > 4:
        os.system('clear')
        print('Número de jogadores inválido')
        QNTD_JOGADORES = int(input('Informe a quantidade de jogadores: '))
    jogadores = []
    for i in range(QNTD_JOGADORES):
        jogadores.append(func.criar_mao(domino, input(f'Informe o nome do jogador {i+1}: ')))
    mesa = tabuleiro()
    for i in jogadores:
        mao_teste = jogadores[i].mao()
        if peca.valor in mao_teste:
            vez = jogadores.index(i)
            break
    print('Jogador {} começa'.format(vez+1))
    while True:
        print('Jogador {} sua vez'.format(vez+1))
        print('Mesa: {}'.format(mesa))
        print('Sua mão: {}'.format(jogadores[vez].mostrar_mao()))
        peca_jogada = input(f'Qual peça deseja jogar? [0-{jogadores[vez].len(mao)}] ')
        if peca_jogada == 'passar':
            vez += 1
            if vez == QNTD_JOGADORES:
                vez = 0
            continue
        else:
            peca_jogada = peca(peca_jogada)
            if func.verificar_peca(mesa, peca_jogada):
                mesa.add_peca(peca_jogada)
                jogadores[vez].tira_peca(peca_jogada)
                if func.verifica_venceu(jogadores[vez]):
                    print('Jogador {} venceu'.format(vez+1))
                    break
                vez += 1
                if vez == QNTD_JOGADORES:
                    vez = 0
                continue
            else:
                print('Peça inválida')
                continue
        
            