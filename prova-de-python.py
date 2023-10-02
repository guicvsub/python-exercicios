'''check point em python'''
print("Seja bem-vindo!")
endereco = input("Digite seu endereço: ")
idade = int(input("Digite sua idade: "))
precov1 = 40
precov2 = 50
precov3 = 50
frete = 5

if idade <= 2005:
    print("Vinho tinto RS 40")
    print("Vinho branco RS 50")
    print("Vinho seco RS 50")
    print("Caso não deseje uma das opções, digite 0")
    
    qtdv1 = int(input("Digite a quantidade de vinho branco: "))
    qtdv2 = int(input("Digite a quantidade de vinho tinto: "))
    qtdv3 = int(input("Digite a quantidade de vinho seco: "))
    
    valortotal = (qtdv1 * precov1) + (qtdv2 * precov2) + (qtdv3 * precov3)
    
    if valortotal > 100:
        print("Você recebeu frete grátis.")
        print(f"Total da sua compra: RS {valortotal}")
    else:
        valortotal += frete
        print(f"Obrigado por comprar! Sua compra é de RS {valortotal} com o frete.")
else:
    print("Não é permitida a venda de bebidas para menores de 18 anos.")

