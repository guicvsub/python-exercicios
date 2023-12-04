'''numero maximo em lista'''
def emcontrar_maior_valor_em_lista(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if (lista[i]) > maior:
            maior = (lista[i])
    return maior

#teste 
num = [0,1,2,3,4]
print(emcontrar_maior_valor_em_lista(num))

    
