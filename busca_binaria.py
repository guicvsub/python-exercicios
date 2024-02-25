def busca_binaria(lista , item):
    baixio = 0
    alto = len(lista) - 1
    while baixio<=alto:
        meio = (alto+baixio) // 2
        chute = lista[meio]
        if chute==item:
            return meio
        if chute > item:
            alto= meio - 1
        else:
            baixio = meio + 1
    return None

minha_lista= [1,3,5,7,9]
a = busca_binaria(minha_lista,9)
print(a)


