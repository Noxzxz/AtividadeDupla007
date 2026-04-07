from Ex001 import Lista

def inserir_processo():
    qtd_processos+=1

    

def main():
    qtd_processos = 1
    lista_processos = Lista()
    
    nome = print(f"Digite o nome do processo {qtd_processos}: ")
    tempo = print(f"Digite o tempo necessário para o processo {qtd_processos}: ")
    novoprocesso = {'id': qtd_processos, 'nome': nome, 'tempo': tempo}
    
    lista_processos.inserir_final(novoprocesso)

if __name__ == "__main__":
    main()