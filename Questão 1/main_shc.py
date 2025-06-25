import oito_rainhas_stochastic_hill_climbing as shc, tabuleiro as tb

if __name__ == "__main__":
    n = 8
    solution = shc.hill_climbing(n)
    tb.gerar_tabuleiro()
    print("Solução encontrada:")
    print("Número de ataques:", shc.count_attacks(solution))