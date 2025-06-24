import random

def print_board(board):
    """
    Imprime o tabuleiro das rainhas.
    'Q' representa uma rainha e '.' representa uma casa vazia.
    """
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def random_board(n):
    """
    Gera uma configuração aleatória de tabuleiro para n rainhas.
    Retorna uma lista onde o índice representa a linha e o valor representa a coluna da rainha.
    """
    return [random.randint(0, n-1) for _ in range(n)]

def count_attacks(board):
    """
    Conta o número de pares de rainhas que se atacam no tabuleiro.
    Considera ataques na mesma coluna e nas diagonais.
    """
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(board):
    """
    Gera todos os vizinhos possíveis do tabuleiro atual,
    movendo cada rainha para todas as outras colunas possíveis em sua linha.
    """
    n = len(board)
    neighbors = []
    for row in range(n):
        for col in range(n):
            if board[row] != col:
                neighbor = list(board)
                neighbor[row] = col
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(n):
    """
    Executa o algoritmo de Hill Climbing para resolver o problema das n rainhas.
    Retorna uma configuração de tabuleiro com o menor número de ataques encontrado.
    """
    current = random_board(n)
    while True:
        neighbors = get_neighbors(current)
        current_attacks = count_attacks(current)
        best_neighbor = min(neighbors, key=count_attacks)
        best_attacks = count_attacks(best_neighbor)
        if best_attacks >= current_attacks:
            return current
        current = best_neighbor

if __name__ == "__main__":
    n = 8
    solution = hill_climbing(n)
    print("Solução encontrada:")
    print_board(solution)
    print("Número de ataques:", count_attacks(solution))