import pandas as pd

def calcular_dias_da_semana(dia_inicio, dias_no_mes):
    dias_da_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
    dias_semana = []

    for dia in range(1, dias_no_mes + 1):
        dia_semana_atual = (dia_inicio + (dia - 1)) % 7
        dias_semana.append(dias_da_semana[dia_semana_atual])

    return dias_semana

def criar_excel(nome_colaborador, dias_no_mes, dia_inicio, primeira_folga):
    dias_semana = calcular_dias_da_semana(dia_inicio, dias_no_mes)

    # Criar o cabeçalho
    cabecalho = ['Dias do mês'] + [str(dia) for dia in range(1, dias_no_mes + 1)]
    df = pd.DataFrame(columns=cabecalho)

    # Adicionar a linha com os dias do mês
    df.loc[0] = [''] + [str(dia) for dia in range(1, dias_no_mes + 1)]

    # Adicionar a linha com os dias da semana
    df.loc[1] = ['Dias da semana'] + dias_semana

    # Calcular as folgas a cada 5 dias
    dias_folga = [primeira_folga + i * 6 for i in range((dias_no_mes - primeira_folga) // 6 + 1) if (primeira_folga + i * 6) <= dias_no_mes]

    # Adicionar a linha com as folgas
    linha_colaborador = [nome_colaborador] + ['F' if dia in dias_folga else '' for dia in range(1, dias_no_mes + 1)]
    df.loc[2] = linha_colaborador

    nome_arquivo = 'folgas.xlsx'
    df.to_excel(nome_arquivo, index=False, header=False)

    print(f'Arquivo "{nome_arquivo}" criado com sucesso!')

# Exemplo de uso
nome_colaborador = input("Digite o nome do colaborador: ")
dias_no_mes = int(input("Digite o número de dias no mês: "))  
dia_inicio = int(input("Digite o dia da semana em que o mês começa (0=segunda, 6=domingo): "))  
primeira_folga = int(input("Digite a data da primeira folga: "))  

criar_excel(nome_colaborador, dias_no_mes, dia_inicio, primeira_folga)