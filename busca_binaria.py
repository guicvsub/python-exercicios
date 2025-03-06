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
    return print(f"o chute {item} nao está na lista" )

minha_lista= [1,3,5,7,9]
lista_ordenada = sorted(minha_lista)
a = busca_binaria(lista_ordenada,18)


print(a)




lista_dois=[("maca", 3),("pitaia", 14),("abacate", 2),("banana", 5)]
tupla_ordenada = sorted(lista_dois, key=lambda x : x[1])
print(tupla_ordenada)


lista_dois=[("maca", 3,"c"),("pitaia", 14,"d"),("abacate", 2,"e"),("banana", 5,"f")]
tupla_ordenada2 = sorted(lista_dois, key=lambda y :(y[1], y[2]))
print(tupla_ordenada2)