import matplotlib.pyplot as plt
def cria_matriz(linhas,colunas):
    matriz=[]
    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

'''def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(0)
        matriz.append(lista)
    return matriz'''

a=cria_matriz(8,8)


def printa_matriz(matriz):
    for linha in matriz:
        print(linha)
    return
printa_matriz(a)


def acessar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j+i)%2==0:
                matriz[i][j]=1
    return matriz
tab=acessar_matriz(a)



plt.imshow(tab)
plt.colorbar()
plt.show()