def acha_maior(lista):
    maior=lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior=lista[i]
    return maior
def acha_indice_maior(lista):
    indice = 0
    maior= lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior= lista[i]
            indice=i
    return indice

caros =["uno","gol","celtinha"]
precos =[10, 20, 1000]
caroMaisCaro = caros[acha_indice_maior(precos)]
precosMaior = acha_maior(precos)
print(f"esse e o carro mais caro e o {caroMaisCaro} e o preco e {precosMaior} ")
ff