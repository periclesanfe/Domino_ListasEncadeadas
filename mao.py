from peca import peca

class mao_jogador:
    def __init__(self, nome):
        self.mao = []
        self.nome = nome
    
    def __str__(self):
        imagem = ''
        for i in range(len(self.mao)):
            imagem += str(self.mao[i]) + ' '
        return imagem
    
    def __len__(self):
        return len(self.mao)
    
    def mao(self):
        imagem = ''
        for i in range(len(self.mao)):
            imagem.append(self.mao[i])
        return imagem
    
    def add_peca(self, peca):
        self.mao.append(peca)
    
    def tira_peca(self, peca):
        return self.mao.pop(peca)
    
    def mostrar_mao(self):
        saida = ''
        for peca in self.mao:
            saida += str(peca) + ' '
        print(saida)