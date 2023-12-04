'''elentos duplicados'''
listareperidos=[]
def checar__elementos__reperidos(lista1,lista2):
    for i in lista1:
        for i2 in lista2:
            if i == i2:
                listareperidos.append(i)
    return listareperidos
print (checar__elementos__reperidos([3,4,5],[6,7,8,4,5]))