import numpy as np
import matplotlib.pyplot as plt

class Decomposicao:
    def __init__(self, matriz):
        self.matriz = matriz
        self.L, self.U = self.LU()

    def LU(self):
        n = len(self.matriz)
        L = np.zeros((n, n))
        U = np.zeros((n, n))

        for j in range(n):
            L[j][j] = 1
            for i in range(j+1):
                soma = sum(L[i][k] * U[k][j] for k in range(i))
                U[i][j] = self.matriz[i][j] - soma

            for i in range(j, n):
                soma = sum(L[i][k] * U[k][j] for k in range(j))
                L[i][j] = (self.matriz[i][j] - soma) / U[j][j]

        return L, U

    def visualizador(self):
        plt.figure(figsize=(8, 6))
        plt.title("Matriz Original")
        plt.imshow(self.matriz, cmap='Greens')
        plt.colorbar()

        plt.figure(figsize=(8, 6))
        plt.title("Matriz L")
        plt.imshow(self.L, cmap='Blues')
        plt.colorbar()

        plt.figure(figsize=(8, 6))
        plt.title("Matriz U")
        plt.imshow(self.U, cmap='Reds')
        plt.colorbar()
        plt.show()


# Implementação
matriz = np.random.randint(1, 10, (14, 14))
decomposicao = Decomposicao(matriz)
decomposicao.visualizador()
