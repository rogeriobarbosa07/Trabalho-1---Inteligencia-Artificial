import random

def chute_inicial():
    return [random.randint(0, 7) for _ in range(8)]

def contar_ataques(posicoes):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if posicoes[i] == posicoes[j] or abs(posicoes[i] - posicoes[j]) == abs(i - j):
                ataques += 1
    return ataques

def gerar_vizinhos(posicoes):
    vizinhos = []
    for col in range(8):
        for linha in range(8):
            if linha != posicoes[col]:
                nova_posicao = posicoes[:]
                nova_posicao[col] = linha
                vizinhos.append(nova_posicao)
    return vizinhos

def hill_climbing_estocastico():
    atual = chute_inicial()
    while True:
        atual_ataques = contar_ataques(atual)
        if atual_ataques == 0:
            return atual
        
        vizinhos = gerar_vizinhos(atual)
        melhores = [v for v in vizinhos if contar_ataques(v) < atual_ataques]

        if not melhores:
            return atual
        
        atual = random.choice(melhores)