import random, copy

def bin_para_dec(bin):
    bin = bin[2:]
    dec = 0
    j = 0
    for i in range(len(bin) - 1, -1, -1):
        if bin[j] == '1':
            dec += 2 ** i
        j += 1
    return dec

def inicializa_populacao():
    pop = []
    for i in range(20):
        pop_i = []
        for j in range(8):
            pop_i.append(bin(random.randint(0, 7)))
        pop.append(pop_i)
    return pop

def calcula_fitness(ind):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if ind[i] == ind[j] or abs(ind[i] - ind[j]) == abs(i - j):
                ataques += 1
    return ataques

def selecao_dos_pais(pop):
    fit_pop = []
    for ind in pop:
        for i in range(8):
            ind[i] = bin_para_dec(ind[i])
        fit_pop.append(calcula_fitness(ind))
    
    for i in range(4):
        fit_pop.pop(max(fit_pop))    

    return fit_pop

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