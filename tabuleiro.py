from peca import peca

class tabuleiro:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.tabuleiro = ''
        
        
    def adiciona_direita(self, nova_peca):
        atual = self.head
        if atual.direita != nova_peca.esquerda:
            nova_peca.inverte_peca()
        atual.next = nova_peca
        nova_peca.prev = atual
        self.head = nova_peca
        self.tabuleiro = self.tabuleiro + str(nova_peca)
                
                
    def adiciona_esquerda(self, nova_peca):
        atual = self.tail
        if atual.esquerda != nova_peca.direita:
           nova_peca.inverte_peca()
        atual.prev = nova_peca
        nova_peca.next = atual
        self.tail = nova_peca
        self.tabuleiro = str(nova_peca) + self.tabuleiro    
            
            
    def adiciona_peca(self, nova_peca):
        if self.head == None:
            self.head = nova_peca
            self.tail = self.head
            self.tabuleiro += str(self.head)
        else:
            if self.tail.esquerda in nova_peca.value:
                self.adiciona_esquerda(nova_peca)
                return
            elif self.head.direita in nova_peca.value:
                self.adiciona_direita(nova_peca)
                return
            else:
                return 'Jogada inválida'
            
    def __str__(self):
        return self.tabuleiro
            
                
                   
            
             # verificar se o valor da esquerda da atual é itual a um dos valores da nova
            # se for igual ao valor da direita da nova, adiciona
            # se for igual ao valor da esquerda da nova, inverte e adiciona
            
            
            
            
    
    
            
                
        
    
    