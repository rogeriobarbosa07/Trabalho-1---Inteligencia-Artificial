import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Criando a matriz 8x8 alternando 0 e 1
tabuleiro = np.zeros((8, 8))
tabuleiro[1::2, ::2] = 1
tabuleiro[::2, 1::2] = 1

# Personalizando o colormap do tabuleiro
colormap_personalizado = ListedColormap(["#f0d9b5", "#a57853"])

fig = plt.figure(figsize=(4, 4), facecolor='white', layout='constrained')
ax = fig.add_subplot()
ax.set_title('Tabuleiro de Xadrez 8x8 com 8 raínhas', fontsize='medium')
ax.imshow(tabuleiro, cmap=colormap_personalizado, extent=[0, 8, 0, 8])

# Posicionando as raínhas
def recebe_rainhas(rainhas):
    for linha, coluna in enumerate(rainhas):
        ax.text(coluna + 0.5, 7.5 - linha, '\u265B', fontsize=32, ha='center', va='center', color='black')

# Removendo os eixos
ax.set_xticks([])
ax.set_yticks([])

def gerar_tabuleiro():
    plt.show()