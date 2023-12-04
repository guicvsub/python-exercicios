'''dedução de uma lista'''
def checar_elementos_repitidos_em_lista(lista):
    lista_filtradda=[]
    for i in lista:
        if i not in lista_filtradda:
            lista_filtradda.append(i)
    return lista_filtradda

#teste da funcao
numeros=[1,2,3,4,5,6,7,8,9,1,2,3,45,67,89,]
print(checar_elementos_repitidos_em_lista(numeros))