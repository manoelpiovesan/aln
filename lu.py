import numpy as np

def show_matrix(mat):
    for row in mat:
        print("|", end="")
        for val in row:
            print(" %.3f" % val, end="")
        print(" |")

def gauss(mat):
    n = len(mat)
    B = np.array([8.30, 3.88, 5.67, 7.73, 4.20, 2.88, 6.45, 3.33, 9.50, 5.20, 8.10, 6.55, 4.25, 7.10])
    M = np.zeros((n, n))
    aux = np.copy(mat)

    print("\n***Seja Aux, uma matriz auxiliar como copia da matriz A***")
    print("----Matriz aux antes----")
    show_matrix(aux)

    for j in range(n):
        print("\n***Multiplicadores da %d coluna***" % (j+1))
        for i in range(j+1, n):
            if aux[i][j] == 0:
                print("Posicao ja e 0, nao ha necessidade de fazer eliminacao de gauss para este termo!")
            else:
                M[i][j] = aux[i][j] / aux[j][j]
                print("M[%d][%d]=%.3f" % (i+1, j+1, M[i][j]))
                for c in range(j, n):
                    aux[i][c] = aux[i][c] + aux[j][c] * (-1*M[i][j])

    print("\n\nRESULTADO FINAL\n")
    for i in range(n):
        M[i][i] = 1
    print("\nMatriz L:\n")
    show_matrix(M)
    print("\nMatriz U:\n")
    show_matrix(aux)

    y = np.zeros(n)
    x = np.zeros(n)

    print("\nnumero de passos: %d\n" % (i-1))
    print("y=")
    for i in range(n):
        soma = np.dot(M[i], y)
        y[i] = ((B[i] - soma) / aux[i][i])
        print("%.3f " % y[i], end="")
    print("\n\nx=")
    for i in range(n-1, -1, -1):
        soma = np.dot(aux[i], x)
        x[i] = ((y[i] - soma) / aux[i][i])
        print("%.3f " % x[i], end="")

    print("\n")


def main():
    A = np.array([[8.27, 7.39, 8.64, 1.98, 5.78, 4.99, 2.34, 7.32, 9.12, 8.55, 3.55, 6.80, 2.68, 3.91],
                  [6.31, -7.05, 2.98, 9.65, 3.44, 5.22, 7.01, 3.24, 1.55, 6.12, 8.77, 9.01, 4.35, 7.21],
                  [3.94, 2.87, 2.33, -2.96, 7.09, 4.22, 8.65, 1.20, 5.78, 6.99, 4.88, 3.77, 2.89, 1.77],
                  [1.48, 4.48, 2.80, 1.52, 3.89, 1.99, 5.22, 8.91, 2.22, 3.55, 4.77, 6.33, 9.12, 8.20],
                  [5.72, 3.44, 6.11, 8.55, 2.77, 9.88, 7.22, 1.99, 6.33, 5.11, 8.99, 7.88, 1.77, 3.55],
                  [4.88, 6.33, 2.11, 3.77, 8.44, 5.11, 3.99, 2.55, 9.99, 8.88, 7.77, 6.22, 4.88, 1.99],
                  [9.33, 7.22, 3.88, 2.99, 4.11, 8.77, 6.55, 4.33, 2.88, 1.11, 5.22, 6.33, 3.44, 8.55],
                  [2.11, 8.88, 5.77, 7.22, 1.99, 3.33, 5.11, 6.88, 8.99, 9.77, 7.22, 5.44, 2.33, 6.11],
                  [1.77, 2.33, 6.99, 5.44, 9.88, 7.22, 3.33, 1.55, 8.88, 4.11, 6.22, 7.77, 9.99, 8.88],
                  [3.88, 2.99, 1.55, 6.77, 4.88, 9.99, 8.55, 5.77, 3.88, 2.99, 1.55, 6.77, 4.88, 9.99],
                  [7.22, 6.33, 4.11, 9.99, 8.88, 7.77, 5.22, 2.33, 1.11, 4.88, 9.77, 3.99, 6.22, 5.33],
                  [5.99, 8.77, 6.22, 1.55, 7.99, 9.77, 3.88, 2.99, 1.55, 6.77, 4.88, 9.99, 8.55, 5.77],
                  [2.33, 1.55, 6.77, 4.88, 9.99, 8.55, 5.77, 7.88, 1.77, 3.33, 5.99, 8.88, 4.88, 9.99],
                  [6.77, 4.88, 9.99, 8.55, 5.77, 7.88, 1.77, 3.33, 5.99, 8.88, 4.88, 9.99, 3.55, 2.22]])

    print("***Seja A a matriz original***")
    print("Matriz A= L * U")
    show_matrix(A)

    gauss(A)

    print("\nMatriz A = L * U")
    show_matrix(A)
    print("\nvetor permutação: [4,3,1,2]\n")


if __name__ == "__main__":
    main()
