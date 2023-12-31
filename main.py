import random
import os

# Classe de exceção para valores inválidos
class ErroValorInvalido(Exception):
    pass

# Classe das peças
class Peca:
    def __init__(self, esquerda, direita):
        self.valor = [esquerda, direita]
        self.esquerda = esquerda # valores de esquerda e direita
        self.direita = direita
        # Estrutura para encadeamento de peças
        self.anterior = None
        self.proximo = None
        
    def __str__(self):
        return f'[{self.esquerda}-{self.direita}]'
    
    def inverte_peca(self):
        self.esquerda, self.direita = self.direita, self.esquerda
        self.valor = [self.esquerda, self.direita]
       
# Classe que representa cada jogador 
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_peca(self, peca):
        self.mao.append(peca)
        
    def retira_peca(self, index):
        self.mao.pop(index)
    
    def mostra_mao(self):
        saida = ''
        for peca in self.mao:
            saida += str(peca) + ' '
        print(f"{self.nome}: {saida}")

# Classe que representa o tabuleiro
class Tabuleiro:
    def __init__(self):
        self.cabeça = None
        self.calda = None
        self.cabeça_valor = None  # Valor da direita da última peça
        self.calda_valor = None  # Valor da esquerda da primeira peça

    def adicionar_peca(self, peca):
        # Verifica se a peça pode ser adicionada às extremidades
        if not self.cabeça: # Se o tabuleiro estiver vazio, a primeira peça pode ser adicionada
            self.cabeça = peca
            self.calda = peca
            self.cabeça_valor = peca.esquerda
            self.calda_valor = peca.direita
            return True
        elif self.cabeça_valor in peca.valor:
            if self.cabeça_valor == peca.esquerda:
                peca.inverte_peca()
            peca.proximo = self.cabeça
            self.cabeça.anterior = peca
            self.cabeça_valor = peca.esquerda
            self.cabeça = peca
            return True
        elif self.calda_valor in peca.valor:
            if self.calda_valor == peca.direita:
                peca.inverte_peca()
            peca.anterior = self.calda
            self.calda.proximo = peca
            self.calda_valor = peca.direita
            self.calda = peca
            return True
        return False

    
    def constroi_saida(self, peca):
        if not peca.proximo:
            return str(peca)
        else:
            return str(peca) + self.constroi_saida(peca.proximo)
      
        
    def __str__(self):
        if not self.cabeça:
            return 'Tabuleiro vazio'
        return self.constroi_saida(self.cabeça)

        

    def verificar_estado_do_jogo(self, jogador, qntd_passes):
        if jogador.mao == []:
            return 0
        elif qntd_passes == 2:
            return 1
        return 2

# Função para criar o conjunto de peças
def criar_conjunto():
    conjunto = []
    for esquerda in range(7):
        for direita in range(esquerda, 7):
            peca = Peca(esquerda, direita)
            conjunto.append(peca)
    random.shuffle(conjunto) # Embaralha as peças
    return conjunto

# Cria as mãos dos jogadores
def distribuir_maos(jogadores, domino_embaralhado):
    for jogador in jogadores:
        for i in range(7):
            jogador.receber_peca(domino_embaralhado.pop())

# mostar domino
def mostrar_domino(domino):
    saida = ''
    for peca in domino:
        saida += str(peca) + ' '
    return saida

while True: # Definir quantidade de jogadores
    num_jogadores = int(input('Digite o número de jogadores: '))
    if 2 <= num_jogadores <= 4:
        break
    os.system('clear')
    print('O número de jogadores deve ser entre 2 e 4')
    continue

jogadores = []
for i in range(num_jogadores):
    nome = input(f'Digite o nome do jogador {i+1}: ')
    jogador = Jogador(nome)
    jogadores.append(jogador)

domino = criar_conjunto()
mostrar_domino(domino)
distribuir_maos(jogadores, domino)
tabuleiro = Tabuleiro()
os.system('clear')

qntd_passes = 0
Estado_do_jogo = 2
while Estado_do_jogo == 2:
    for i in range(0, len(jogadores)):
        jogador_vez = jogadores[i]
        print(f'Vez do jogador {jogador_vez.nome}')
        print(f'Tabuleiro: {tabuleiro}')
        jogador_vez.mostra_mao()
        while True:
            try:
                peca_escolhida = int(input('Digite o número da peça que deseja jogar: '))
                if peca_escolhida == 0:
                    qntd_passes += 1
                    os.system('clear')
                    break
                elif 1 <= peca_escolhida <= len(jogador_vez.mao):
                    if tabuleiro.adicionar_peca(jogador_vez.mao[peca_escolhida-1]):
                        remover = jogador_vez.mao.pop(peca_escolhida -1)
                        qntd_passes = 0
                        os.system('clear')
                    break
                else:
                    raise ErroValorInvalido
            except ErroValorInvalido:
                print('Valor inválido')
                continue
            
        Estado_do_jogo = tabuleiro.verificar_estado_do_jogo(jogador_vez, qntd_passes)
        if Estado_do_jogo == 0:
            print(f'O jogador {jogador_vez.nome} venceu!')
            break
        elif Estado_do_jogo == 1:
            print('O jogo empatou!')
            break
        elif Estado_do_jogo == 2:
            continue
        
        if i == len(jogadores) - 1:
            i = -1
