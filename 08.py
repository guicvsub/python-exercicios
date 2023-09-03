nl=int(input("digite o numero de lados "))
if nl>5:
    print("poligono desconhecido")
if nl==3:
    print("e um triangulo")
    cm = int(input("digite a area"))
    print(f"o valor da area e {(((cm*cm))*(1.73)) / 4} cm ")
elif nl==4:
     cm = int(input("digite a area"))
     print(f"e um quadrado {(cm*cm)} cm ")
elif nl==5:
    print("e um poligono")
else:
    print("nao e um poligano ")