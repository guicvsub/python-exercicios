print("*********************")
print(" jogo de adivinhação ")
print("*********************")
contador = 5
numero_secreto = 42
chute = int(input("digite um numero "))
maior = chute > numero_secreto
menor = chute < numero_secreto
acertou = chute ==numero_secreto
while  (chute!=acertou and contador > 0):

 print ("acertou o número secreto era",numero_secreto)
 if(acertou):
    print("voce errou") 
 if (menor):
  print("digite um numero menor")
  contador-=1 
  chute = int(input("digite um numero "))
 else:
    print("digite um numero maior")
    contador-=1 
    chute = int(input("digite um numero "))