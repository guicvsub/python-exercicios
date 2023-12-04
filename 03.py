def invertendo_ordem_da_lista(lista):
    lista_invertida=[]
    tamanho=len(lista)
    for i in range(tamanho // 2):
        lista_invertida.append(lista[tamanho -1 -i])
        lista_invertida.append(lista[i])
    return lista_invertida

minhaLista=[0,1]

print(invertendo_ordem_da_lista(minhaLista))