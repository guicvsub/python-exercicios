print("*********************")
print(" jogo de adivinhação ")
print("*********************")
numero_secreto = 42
chute = int(input("digite um numero "))
maior = chute > numero_secreto
menor = chute < numero_secreto
acertou = chute ==numero_secreto
if (acertou):

 print ("acertou o número secreto era",numero_secreto)
else :
 print("voce errou") 
if (menor):
 print("digite um numero menor")
else:
 print("digite um numero maior")
                        