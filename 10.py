l1=int(input("digite o lado 1"))
l2=int(input("digite o lado 1"))
l3=int(input("digite o lado 1"))
if l1 == l2 == l3: 
    print("esse triangulo e equilatero")
elif l1==l2 or l1==l3 or l2==l3:
    print("esse triangulo issosceles")
else:
    print("esse triangulo e escaleno")