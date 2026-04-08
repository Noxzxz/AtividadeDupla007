from Ex001 import Lista

def main():
    lista_processos = Lista()
    relatorio = []
    
    qtd_processos = int(input(f"Quantos processos você deseja registrar?"))
    for i in range(qtd_processos):
        nome = input(f"Digite o nome do processo {i+1}: ")
        tempo = input(f"Digite o tempo necessário para o processo {i+1}: ")
        novoprocesso = {'id': i, 'nome': nome, 'tempo_total': int(tempo), 'tempo_restante': int(tempo)}        
        lista_processos.inserir_final(novoprocesso)
    
    tempo_processos = int(input(f"Digite a quantidade de unidades de tempo que a CPU executará cada processo:"))
    
    contador_tempo = 0
    
    while lista_processos.tamanho > 0:
        processo = lista_processos.inicio.dado
        
        if processo['tempo_restante'] < tempo_processos:
            tempo_a_passar = processo['tempo_restante']
        else:
            tempo_a_passar = tempo_processos
        
        processo['tempo_restante'] -= tempo_a_passar
        contador_tempo += tempo_a_passar
        
        if processo['tempo_restante'] == 0:
            print(f"t = {contador_tempo - tempo_a_passar} - {processo['nome']} executa {tempo_a_passar}u | CONCLUÍDO (terminou em t={contador_tempo})")
            
            relatorio.append({
                'nome': processo['nome'],
                'tempo_total': processo['tempo_total'],
                'tempo_retorno': contador_tempo,
                'tempo_espera': contador_tempo - processo['tempo_total']
            })
            lista_processos.remover(processo)
        else:
            print(f"t = {contador_tempo - tempo_a_passar} → {processo['nome']} executa {tempo_a_passar}u | restam: {processo['tempo_restante']}u")
            lista_processos.remover(processo)
            lista_processos.inserir_final(processo)
    
    total_espera = 0
    total_retorno = 0
    
    for r in relatorio:
        print(f"  {r['nome']:<15} {str(r['tempo_total'])+'u':>10} {str(r['tempo_espera'])+'u':>10} {str(r['tempo_retorno'])+'u':>10}")
        total_espera += r['tempo_espera']
        total_retorno += r['tempo_retorno']
 
    media_espera = total_espera / len(relatorio)
    media_retorno = total_retorno / len(relatorio)
    
    
    print("-" * 52)
    print(f"  {'Média':<15} {'-':>10} {media_espera}u {media_retorno}u")
    print("=" * 52)
 
    if media_espera < 16:
        print(f"\nARIA reativada com sucesso.")
        print(f"Tempo médio de espera ({media_espera}) abaixo do limite crítico (16u).")
        print("Synthetica está salva.")
    else:
        print(f"\nFalha crítica confirmada. Protocolo de desligamento de emergência.")
        
if __name__ == "__main__":
    main()