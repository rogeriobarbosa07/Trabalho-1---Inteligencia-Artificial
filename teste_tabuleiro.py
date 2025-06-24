import matplotlib.pyplot as plt
import numpy as np

tabuleiro = np.zeros((8, 8))
tabuleiro[1::2, ::2] = 1
tabuleiro[::2, 1::2] = 1

fig = plt.figure(figsize=(4, 4), facecolor='lightskyblue', layout='constrained')
fig.suptitle('Tabuleiro')
ax = fig.add_subplot()
ax.set_title('Tabuleiro de Xadrez', loc='left', fontstyle='oblique', fontsize='medium')
ax.imshow(tabuleiro, cmap='gray', extent=[0, 8, 0, 8])

ax.set_xticks([])
ax.set_yticks([])

plt.show()