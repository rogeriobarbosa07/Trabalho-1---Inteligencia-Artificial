import random, copy

def inicializa_populacao():
    pop = []
    for i in range(20):
        pop_i = []
        for j in range(8):
            pop_i.append(bin(random.randint(0, 7)))
        pop.append(pop_i)
    return pop

def calcula_fitness(pop):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if int(pop[i]) == int(pop[j]) or abs(int(pop[i]) - int(pop[j])) == abs(i - j):
                ataques += 1
    return ataques

def selecao_dos_pais(pop):
    corte = random.randint(1, 7)

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