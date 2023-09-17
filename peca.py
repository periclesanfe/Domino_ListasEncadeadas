class peca:
    def __init__(self, value):
        self.value = value
        self.esquerda = value[0]
        self.direita = value[2]
        self.next = None
        self.prev = None
    
    def valor(self):
        return self.value
    
    def __str__(self):
        return f'[{self.esquerda}-{self.direita}]'
    
    
    def inverte_peca(self):
        self.esquerda, self.direita = self.direita, self.esquerda
        self.value = (self.esquerda, self.direita)
        
    
    