class Caixa:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def e_uma_caixa(self):
        return isinstance(self.conteudo, list)

    def e_uma_chave(self):
        return self.conteudo == "chave"

def procure_pela_chave(caixa_principal):
    pilha = []
    pilha.append(caixa_principal)
    while pilha:
        caixa = pilha.pop()
        for item in caixa:
            if isinstance(item, Caixa) and item.e_uma_caixa():
                pilha.append(item)
            elif isinstance(item, Caixa) and item.e_uma_chave():
                print("Achei a chave!")
                return

# Exemplo de uso
caixa_principal = [
    "livro",
    "roupas",
    [Caixa("caderno"), Caixa("caneta"), Caixa("chave")],
    "brinquedo"
]

procure_pela_chave(caixa_principal)
