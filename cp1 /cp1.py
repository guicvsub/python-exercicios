def separar_equipamentos(dicionario_equipamentos):
    pendentes = []
    concluídos = []
    
    for status, equipamentos in dicionario_equipamentos.items():
        if status == 0:
            pendentes.extend(equipamentos)  # Adiciona os equipamentos pendentes
        elif status == 1:
            concluídos.extend(equipamentos)  # Adiciona os equipamentos concluídos
    
    return pendentes, concluídos


dicionario_equipamentos = {
    0: [101, 103, 105, 108],  
    1: [102, 104, 106, 107]  
}

# Chamando a função e recebendo as listas
pendentes, concluídos = separar_equipamentos(dicionario_equipamentos)


print("Pendentes:", pendentes)
print("Concluídos:", concluídos)




def categorizar_produtos():
    # Listas para armazenar os produtos de cada categoria
    aprovados = []
    reprovados = []
    pendentes = []
    
    # Coletando dados do usuário
    for i in range(1, 11):
        numero_serie = input(f"Digite o número de série do produto {i}: ")
        status = int(input(f"Digite o status de qualidade para o produto {numero_serie} (1 = aprovado, 0 = reprovado, -1 = pendente): "))
        
        # Categorizar de acordo com o status
        if status == 1:
            aprovados.append(numero_serie)
        elif status == 0:
            reprovados.append(numero_serie)
        elif status == -1:
            pendentes.append(numero_serie)
        else:
            print("Status inválido! Digite 1 para aprovado, 0 para reprovado, ou -1 para pendente.")
            continue
    
    # Exibindo os resultados
    print("\nProdutos Aprovados:", aprovados)
    print("Produtos Reprovados:", reprovados)
    print("Produtos Pendentes:", pendentes)

# Chamando a função
categorizar_produtos()
