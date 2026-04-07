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
            print(aux.dado, end=" ")
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
        pos = 0
        while aux:
            if aux.dado.nome == valor:
                return print(f"Nome:{aux.dado.nome} |Prioridade: {aux.dado.prior} | Posição: {pos}")
            aux = aux.dir
            pos+=1
        return ("Não encontrado")
    
    def atender(self):
        aux = self.inicio
        if self.tamanho == 1: # a lista tem apenas um valor
            self.inicio = None
            self.fim = None   
        else:
            aux.dir.esq = None
            self.inicio = aux.dir
            aux.dir = None   
                     
        aux = None
        self.tamanho -= 1      
        return print(f"Nome: {self.inicio.dado.nome}| Prioridade: {self.inicio.dado.prior}")          
                
lista = Lista()

i = 0
while i != 5:
    
    match i:
        case 0:
            i = int(input("1 - Inserir paciente\n2 - Imprimir listar de pacientes\n3 - Buscar paciente\n4 - Atender paciente\n5 - Sair\n"))
        case 1:
            nome = input("Insira o nome do paciente: ")
            prior = int(input("Insira o grau de prioridade \n0 - normal | 1 - prioridade\n"))
            lista.inserir_final(Paciente(nome, prior))
            i=0
            print("\n")
        case 2:
            lista.imprimir()
            i=0
            print("\n")
        case 3:
            nome = input("Insira o nome a ser buscado: ")
            lista.pesquisar(nome)
            i=0
            print("\n")
        case 4:
            lista.atender()
            i=0
            print("\n")
        case 5:
            i = 5
            break
        case _:
            print("Insira um valor valido")
            i=0
            print("\n")