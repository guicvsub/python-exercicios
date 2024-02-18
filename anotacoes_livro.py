'''• A pesquisa binária é muito mais rápida do que a pesquisa simples.
• O(log n) é mais rápido do que O(n), e O(log n) ca ainda mais rápido
conforme os elementos da lista aumentam.
• A rapidez de um algoritmo não é medida em segundos.
• O tempo de execução de um algoritmo é medido por meio de seu
crescimento.
• O tempo de execução dos algoritmos é expresso na notação Big O'''

'''Usar um array signica que todas as suas tarefas estão armazenadas
contiguamente (uma ao lado da outra) na memória.'''
'''array muito lento na armazenagem de novos itens ´porem voce pode reservar lugar que nao serao ocupador naquele 
momento para futuras adicoes  sem precisar mover '''
'''• Você pode não precisar dos espaços extras que reservou; então a memória
será desperdiçada. Você não está utilizando a memória, mas ninguém
mais pode usá-la também.
• Você pode precisar adicionar mais de dez itens a sua lista de tarefas, então
você terá de mover seus itens de qualquer maneira.
Embora seja uma boa forma de contornar o problema, não é uma solução
perfeita. Listas encadeadas resolvem este problema de adição de itens.
'''