class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def imprimir(self):
        aux = self.inicio
        i=0
        while aux:
            print(aux.dado, end="  ")
            aux = aux.dir
            i+=1
            if(i>=self.tamanho):
                break
    
    def inserir_final(self, valor):
        novo = No(valor)
        
        # verifica se a lista está vazia
        if self.tamanho == 0:            
            self.inicio = novo          
        else:
           self.fim.dir = novo
           novo.esq = self.fim
           #teste
           self.fim.esq = novo.esq
           novo.dir = self.fim.esq
           
        self.fim = novo        
        self.tamanho += 1       
    
    def pesquisar(self, valor):
        aux = self.inicio
        while aux:
            if aux.dado == valor:
                return aux
            aux = aux.dir
        return None
    
    def remover(self, valor):
        aux = self.pesquisar(valor)
        
        if aux is not None:
            if self.tamanho == 1: # a lista tem apenas um valor
                self.inicio = None
                self.fim = None                
            elif aux == self.inicio: # remove o primeiro elemento
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None           
            elif aux == self.fim: # remove o último elemento
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
                print("KARALHO")
            aux = None
            self.tamanho -= 1    
            

listaEnc = Lista()

listaEnc.inserir_final(10)
listaEnc.inserir_final(20)
listaEnc.inserir_final(30)

listaEnc.imprimir()
listaEnc.remover(20)
print("")
listaEnc.imprimir()
print("")
listaEnc.inserir_final(40)
listaEnc.imprimir()