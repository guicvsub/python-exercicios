'''criando função que retona pares de uma lista'''
def encontra_pares_em_lista(lista):
    pares = 0
    nova__lista=[]
    for num in lista:
        if num %2==0:
            nova__lista.append(num)
    return nova__lista 
print(encontra_pares_em_lista([1,3,4,5,6]))
