from peca import peca

class mao_jogador:
    def __init__(self):
        self.mao = []
    
    def __str__(self):
        imagem = ''
        for i in range(len(self.mao)):
            imagem += str(self.mao[i]) + ' '
        return imagem
    
    def add_peca(self, peca):
        self.mao.append(peca)
    
    def tira_peca(self, peca):
        return self.mao.pop(peca)
    