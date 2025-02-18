lista = [10,20,30,40]
alvo = 30
indice =0
for i in range(len(lista)-1):
    if alvo == lista[i]:
        indice= i
        print(f"entrei o alvo {alvo} o indice e {indice}")