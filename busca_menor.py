def busca_menor(lista):
    indice= 0
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor= lista[i]
            indice = i
    return indice

lista= [4,5,1]
a = lista[busca_menor(lista)]
print(a)

def ordenacao_por_seleçao(lista):
    lista_ordenada=[]
    for i in range(len(lista)):
        menor = busca_menor(lista)
        lista_ordenada.append(lista.pop(menor))
    return lista_ordenada
listaDesordenada=[100,99,85,16,41,50,1,2,7]
lista_ordenada=ordenacao_por_seleçao(listaDesordenada)
print(lista_ordenada)