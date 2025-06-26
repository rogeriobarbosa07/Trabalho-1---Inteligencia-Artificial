import copy
import random

def chute_inicial():
    return [random.randint(0, 7) for _ in range(8)]

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

def hill_climbing_estocastico():
    posicoes = chute_inicial()
    melhorou = True
    while conta_ataques(posicoes) > 0:
        if not melhorou:
            posicoes = chute_inicial()
        melhorou = False
        for i in range(8):
            melhores = melhores_vizinhos(posicoes, i)
            if len(melhores) > 0:
                posicoes[i] = random.choice(melhores)
                melhorou = True
    return posicoes