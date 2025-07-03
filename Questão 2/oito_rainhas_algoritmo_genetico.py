import random, copy

def conta_ataques(posicoes):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if posicoes[i] == posicoes[j] or abs(posicoes[i] - posicoes[j]) == abs(i - j):
                ataques += 1
    return ataques

def melhores_vizinhos(posicoes, n):
    melhores = []
    for i in range(8):
        posicoes_copia = copy.deepcopy(posicoes)
        posicoes_copia[n] = i
        if conta_ataques(posicoes_copia) < conta_ataques(posicoes):
            melhores.append(i)
    return melhores

def inicializa_populacao():
    pop = []
    for i in range(20):
        pop_i = []
        for j in range(8):
            pop_i.append(bin(random.randint(0, 7)))
        pop.append(pop_i)
    return pop

def selecao_dos_pais(pop):

    return

'''
PSEUDOCÓDIGO:

p = inicializa_populacao()
fp = calcula_fitness()

while(critério de parada não é alcançado):
    p' = selecao_dos_pais({p, fp})
    p" = cruzamento(p')
    p"' = mutacao(p")
    fp"' = calcula_fitness(p"')
    {p, fp} = selecao_dos_sobreviventes({p, fp}, {p"', fp"'})

return melhor_solucao(p)
'''