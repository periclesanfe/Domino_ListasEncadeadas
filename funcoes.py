from random import randint
from mao import mao_jogador
from peca import peca
# aqui vai ficar as funções
# Função para criar um conjunto de peças de dominó
def criar_domino():
  array = [ peca('0:1'), peca('0:2')
            # peca[0, 2], peca[0, 3], peca[0, 4], peca[0, 5], peca[0, 6], peca[1, 1], peca[1, 2], peca[1, 3], peca[1, 4], peca[1, 5], peca[1, 6], peca[2, 2], peca[2, 3], peca[2, 4], peca[2, 5], peca[2, 6], peca[3, 3], peca[3, 4], peca[3, 5], peca[3, 6], peca[4, 4], peca[4, 5], peca[4, 6], peca[5, 5], peca[5, 6], peca[6, 6]
            ]
  return array
#Funçao para embaralhar um domino

def embaralhar_domino(domino):
  for i in range(28):
    n1 = randint(0,27)
    n2 = randint(0,27)
    domino[n1], domino[n2] = domino[n2], domino[n1]
  return domino


def criar_mao(domino):
  mao = mao_jogador()
  for i in range(7):
    mao.add_peca(domino.pop(randint(0,len(domino)-1)))
  return mao

if __name__ == "__main__":
  domino = criar_domino()
  saida = ''
  for i in domino:
    saida += str(i) + ' '
  print(saida)
