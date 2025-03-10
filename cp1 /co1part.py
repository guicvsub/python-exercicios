def cria_listas():
    lista_equipamentos = list(range(101, 109))
    lista_manutencao = [0, 1, 0, 1, 0, 1, 1, 0]
    return lista_equipamentos, lista_manutencao

# Chamando a função
codigos_equipamentos, status_manutencao = cria_listas()

equip_pendentes, equip_concluidos = separar_equipamentos(codigos_equipamentos, status_manutencao)

# Exibindo os resultados
print("Equipamentos pendentes:", equip_pendentes)
print("Equipamentos concluídos:", equip_concluidos)
