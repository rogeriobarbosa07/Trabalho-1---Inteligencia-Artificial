import random, copy

# Conversões de bases
def bin_para_dec(bin): # Função para modifcar a string binária para números em decimal
    dec = 0
    j = 0
    for i in range(len(bin) - 1, -1, -1):
        if bin[j] == '1':
            dec += 2 ** i
        j += 1
    return dec

def dec_para_bin(dec):
    bin_ = bin(dec)[2:]
    bin_3 = list(bin_.zfill(3)) # garante 3 bits
    bin_3 = ''.join(bin_3)
    return bin_3

# Gera uma população inicial aleatória
def inicializa_populacao():
    pop = []
    for i in range(20):
        pop_i = []
        for j in range(8):
            pop_i.append(dec_para_bin(random.randint(0, 7)))
        pop.append(pop_i)
    return pop

# FUNÇÃO QUE RETORNA O FITNESS!
def calcula_fitness(pop):
    pop_copia = copy.deepcopy(pop)
    fit_pop = []
    dec_pop = []

    for ind in pop_copia:
        for i in range(8):
            ind[i] = bin_para_dec(ind[i])
        dec_pop.append(ind)

        ataques = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if ind[i] == ind[j] or abs(ind[i] - ind[j]) == abs(i - j):
                    ataques += 1

        fit = 1/(1 + ataques) # melhor fitness: 1
        fit_pop.append(fit)
    
    return fit_pop

# Seleciona os pais (com base na roleta)
def selecao_dos_pais(pop, fit_pop):
    pop_copia = copy.deepcopy(pop)

    dec_pop = []
    for ind in pop_copia:
        for i in range(8):
            ind[i] = bin_para_dec(ind[i])
        dec_pop.append(ind)

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
                    pais[j][k] = dec_para_bin(pais[j][k])
                j += 1
                break

    return pais

# Função do cruzamento: utiliza a estratégia do ponto de corte
def cruzamento(pop, fit_pop):
    filhos = []

    for _ in range(8): # taxa de cruzamento: 80%
        pais = selecao_dos_pais(pop, fit_pop)
        corte = random.randint(1, 7)

        filho1 = pais[0][:corte] + pais[1][corte:]
        filho2 = pais[0][corte:] + pais[1][:corte]

        filhos.append(filho1)
        filhos.append(filho2)

    return filhos

# Função de mutação: utiliza a estratégia do bitflip
def mutacao(pop):
    pop_copia = copy.deepcopy(pop)
    for i in range(len(pop_copia)):
        for j in range(8):
            bin = list(pop_copia[i][j])
            for k in range(len(bin)):
                flip = random.randint(1, 100)
                if flip <= 3: # taxa de mutação: 3%
                    if bin[k] == '0':
                        bin[k] = '1'
                    if bin[k] == '1':
                        bin[k] = '0'
            pop_copia[i][j] = ''.join(bin)
    return pop_copia

# Seleciona os indivíduos mais adaptados (com base no fitness)
def selecao_elitista(pop, fit_pop):
    pop_copia = copy.deepcopy(pop)
    fit_pop_copia = copy.deepcopy(fit_pop)

    for i in range(8):
        pos_menor = 0
        for j in range(19):
            if fit_pop[j] > fit_pop[j + 1]:
                pos_menor = j + 1
        pop_copia.pop(pos_menor)
        fit_pop_copia.pop(pos_menor)

    return pop_copia, fit_pop

# Execução do algoritmo!
def algoritmo_genetico():
    pop = inicializa_populacao() 
    fit_pop = calcula_fitness(pop)
    for i in range(1000):
        if 1 in fit_pop:
            pos_ideal = fit_pop.index(1)
            print("Indivíduo ideal: ", pop[pos_ideal])
            break
        
        pop_mais = pop + cruzamento(pop, fit_pop)
        pop_mut = mutacao(pop_mais)
        fit_mut = calcula_fitness(pop_mut)
        pop, fit_pop = selecao_elitista(pop_mut, fit_mut)

if __name__ == '__main__':
    algoritmo_genetico()

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