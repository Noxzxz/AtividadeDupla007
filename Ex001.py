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
        for _ in range(self.tamanho):
            print(aux.dado, end="  ")
            aux = aux.dir
    
    def inserir_final(self, valor):
        novo = No(valor)
        
        # verifica se a lista está vazia
        if self.tamanho == 0:            
            self.inicio = novo          
        else:
           self.fim.dir = novo
           novo.esq = self.fim
           #teste circulo
           self.inicio.esq = novo
           novo.dir = self.inicio
           
        self.fim = novo        
        self.tamanho += 1     

    def inserir_posi(self, valor, posic):
        novo = No(valor)
        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
        elif posic == 0:
            self.inicio.esq = novo
            novo.dir = self.inicio

            self.fim.dir = novo
            novo.esq = self.fim
            self.inicio = novo


        elif posic == self.tamanho:
            self.inserir_final(valor)

        else:
            for _ in range(posic):
                if _ == 0:
                    Proc = self.inicio
                else:
                    Proc = Proc.dir 
            
            ant = Proc.esq
            novo.esq = ant
            novo.dir = Proc
            Proc.esq = novo
            ant.dir = novo

        self.tamanho+=1

    
    def pesquisar(self, valor):
        aux = self.inicio
        for _ in range(self.tamanho):
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
                #circulo
                aux.dir.esq = self.fim
                self.inicio = aux.dir
                aux.dir = None  
                
            elif aux == self.fim: # remove o último elemento
                #circulo
                aux.esq.dir = self.inicio
                self.fim = aux.esq
                aux.esq = None
                
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
                print("KARALHO")#mecanismo alta qualidade para rastreio
            aux = None
            self.tamanho -= 1    

def main():
    listaEnc = Lista()

    listaEnc.inserir_final(10)
    listaEnc.inserir_final(20)
    listaEnc.inserir_final(30)
    listaEnc.imprimir()
    print("")

    listaEnc.remover(10) 
    listaEnc.imprimir()
    print("")

    listaEnc.remover(30)
    listaEnc.imprimir()
    print("")

    listaEnc.remover(20)
    listaEnc.imprimir()    
            
if __name__ == "__main__":
    main()