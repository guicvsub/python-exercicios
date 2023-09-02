nl=int(input("digite o numero de lados "))
cm = int(input("digite a area"))
if nl==3:
    print("e um triangulo")
    print(f"o valor da area e {((cm*cm)*(1.73)) / 4} cm ")
elif nl==4:
    print(f"e um quadrado {(nl*nl)} cm ")

elif nl==5:
    print("e um poligono")
else:
    print("poligono desconhecido")

