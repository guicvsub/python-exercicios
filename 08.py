nl=int(input("digite o numero de lados "))
if nl>5:
    print("poligono desconhecido")
if nl==3:
    print("e um triangulo")
    print(f"o valor da area e {((cm*cm)*(1.73)) / 4} cm ")
    cm = int(input("digite a area"))
elif nl==4:
    print(f"e um quadrado {(nl*nl)} cm ")
    cm = int(input("digite a area"))
elif nl==5:
    print("e um poligono")
else:
    print("nao e um poligano ")