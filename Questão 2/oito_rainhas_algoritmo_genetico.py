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
    fit_filhos = []
    dec_filhos = []

    for _ in range(8): # taxa de cruzamento: 80%
        pais = selecao_dos_pais(pop)
        corte = random.randint(1, 7)

        filho1 = pais[0][:corte] + pais[1][corte:]
        filho2 = pais[0][corte:] + pais[1][:corte]

        filhos.append(filho1)
        filhos.append(filho2)

    for ind in filhos:
        for i in range(8):
            ind[i] = bin_para_dec(ind[i])
        dec_filhos.append(ind)
        ataques = calcula_fitness(ind)
        fit = 1/(1 + ataques)
        fit_filhos.append(fit)

    return filhos, fit_filhos

def mutacao(pop):
    for i in range(len(pop)):
        for j in range(8):
            bin = pop[i][j][2:]
            bin_3 = list(bin.zfill(3)) # garante 3 bits
            for k in range(len(bin_3)):
                flip = random.randint(1, 100)
                if flip <= 3: # taxa de mutação: 3%
                    if bin[k] == '0':
                        bin[k] = '1'
                    if bin[k] == '1':
                        bin[k] = '0'
            pop[i][j] = '0b' + ''.join(bin_3)
    return pop

def selecao_elitista(pop):
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