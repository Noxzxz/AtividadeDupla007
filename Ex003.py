class Paciente:
    def __init__(self, nome:str, prior: int):
        self.nome = nome
        #vou separar prioridade de forma binaria com prioridade 0 e 1 respectivamente, sem prioridade e prioridade
        self.prior = prior


    def __str__(self):
        return (f"Nome:{self.nome} | Prioridade:{self.prior}")

class No:
    def __init__(self, dado: Paciente):
        self.dado = dado
        self.esq = None
        self.dir = None

    def __str__(self):
        return (f"Nome:{self.dado.nome} | Prioridade:{self.dado.prior}")
        
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def imprimir(self):
        aux = self.inicio
        while aux:
            print(aux.dado, end="  ")
            aux = aux.dir
            print("")
    
    def inserir_final(self, valor):
        novo = No(valor)
        
        # verifica se a lista está vazia
        if self.tamanho == 0:            
            self.inicio = novo  
            self.fim = novo
                
        elif(valor.prior==0): #verificar prioridade
           self.fim.dir = novo
           novo.esq = self.fim
           self.fim = novo
           
        else:
            aux = self.inicio
            while aux and aux.dado.prior != 0: #percorre a lista ate entrar na parte de não prioritario
                aux = aux.dir
                
            if aux is None: #todos prioridade 1
                self.fim.dir = novo
                novo.esq = self.fim
                self.fim = novo
                
            elif aux == self.inicio:
                novo.dir = self.inicio
                self.inicio.esq  = novo
                self.inicio = novo
                
            else:
                aux.esq.dir = novo
                novo.esq = aux.esq
                novo.dir = aux
                aux.esq = novo
              
        self.tamanho += 1       
    
    def pesquisar(self, valor):
        aux = self.inicio
        while aux:
            if aux.dado.nome == valor:
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
            aux = None
            self.tamanho -= 1                
                
lista = Lista()

lista.inserir_final(Paciente("ihan",1))
lista.inserir_final(Paciente("Ihago",0))

lista.imprimir()

lista.inserir_final(Paciente("caralho",1))
lista.inserir_final(Paciente("porra",0))
lista.inserir_final(Paciente("jumento",0))
lista.inserir_final(Paciente("candango",1))
lista.inserir_final(Paciente("Paraiba",1))
lista.inserir_final(Paciente("Fud",0))

print("Divi")
lista.imprimir()