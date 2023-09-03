ang1=int(input("digite o valor do primeiro angulo"))
ang2=int(input("digite o valor do primeiro angulo"))
ang3=int(input("digite o valor do primeiro angulo"))
tv=ang1+ang2+ang3
if tv == 180:
    if ang1==90 or ang2==90 or ang3==90:
        print("triangulo retagulo, possui um angulo reto ")
    elif ang1>90 or ang2>90 or ang3>90:
        print("triangulo obtusangulo, possui angulo obtuso")
    elif ang1<90 and ang2<90 and ang3<90:
        print("triangulo acutangulo, possui angulo menor do que 90º ")
else:
    print("triangulo invalido")