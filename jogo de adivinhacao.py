print("*********************")
print(" jogo de adivinhação ")
print("*********************")
numero_secreto = 42
chute = int(input("digite um numero "))
if chute==numero_secreto:
    print ("acertou o número secreto era",numero_secreto)
else :
    print("voce errou")
    if numero_secreto > chute:
                print("digite um numero menor")
    else:
        print("digite um numero maior")
                        