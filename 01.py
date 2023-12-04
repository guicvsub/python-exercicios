'''1 criando uma função que soma uma lista '''
def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma
print(soma_lista([1, 2, 3, 4, 5])) # Saída: 15