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
