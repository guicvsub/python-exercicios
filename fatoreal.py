def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero_base = int(input("Digite o número para calcular o fatorial: "))
resultado_fatorial = fatorial(numero_base)
print(f"O fatorial de {numero_base} é: {resultado_fatorial}")




















