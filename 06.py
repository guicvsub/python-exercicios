sexo=int(input("fdigite 1 para masculino ou 2 para feminino"))
altura=float(input("digite a sua altura"))
if sexo ==1:
    print(F"seu peso ideal e {((72.7*altura) - 58)}")
else:
    print(F'seu peso ideal e {((62.1*altura) - 44.7 )}')