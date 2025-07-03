import random, copy

def bin_para_dec(bin): # Função para modifcar a string binária para números em decimal
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
    dec_pop = []

    # Converte e calcula o fitness dos indivíduos
    for ind in pop:
        for i in range(8):
            ind[i] = bin_para_dec(ind[i])
        dec_pop.append(ind)
        ataques = calcula_fitness(ind)
        fit = 1/(1 + ataques)
        fit_pop.append(fit)

    soma_fit = sum(fit_pop)

    pais = []
    j = 0
    for _ in range(2):
        r = random.uniform(0, soma_fit)
        soma = 0
        for i, fit in enumerate(fit_pop):
            soma += fit
            if soma >= r:
                pais.append(copy.deepcopy(dec_pop[i]))
                for k in range(8):
                    pais[j][k] = bin(pais[j][k])
                j += 1
                break

    return pais

def cruzamento(pop):
    filhos = []
    for _ in range(8): # taxa de cruzamento: 80%
        pais = selecao_dos_pais(pop)
        corte = random.randint(1, 7)

        filho1 = pais[0][:corte] + pais[1][corte:]
        filho2 = pais[0][corte:] + pais[1][:corte]

        filhos.append(filho1)
        filhos.append(filho2)
    return filhos

def mutacao(pop):
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