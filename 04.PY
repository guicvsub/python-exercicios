'''comprimento da lista (SEM LEN)'''
def comprimento_da_lista(lista):
    comprimento = 0 
    for i in lista:
        comprimento += 1
    return comprimento     

LISTTESTE = [0,1,2]
print("Comprimento da lista: ", comprimento_da_lista(LISTTESTE))