import numpy as np

# Função para calcular o determinante de uma matriz 3x3

matriz = np.array([[1, 2, 3], [0,1, 4], [5, 6, 0]])
print(matriz)

def calcular_determinante(matriz):

    if matriz.ndim != 2 or matriz.shape != (3, 3):
        print("Sinto muito. Você não inseriu uma matriz 3x3.")

    else:
        print("Perfeito. Você inseriu uma matriz 3x3 adequadamente.")

    primeira_coluna = matriz[0:3, 0]
    segunda_coluna = matriz[0:3, 1]

    nova_coluna = np.column_stack((matriz, primeira_coluna))
    matriz_expandida = np.column_stack((nova_coluna, segunda_coluna))

    diagonal_principal_1 = matriz_expandida[[0, 1, 2], [0, 1, 2]]
    diagonal_principal_2 = matriz_expandida[[0, 1, 2], [1, 2, 3]]
    diagonal_principal_3 = matriz_expandida[[0, 1, 2], [2, 3, 4]]

    diagonais_principais = [diagonal_principal_1, diagonal_principal_2, diagonal_principal_3]

    diagonal_secundaria_1 = matriz_expandida[[0, 1, 2], [2, 1, 0]]
    diagonal_secundaria_2 = matriz_expandida[[0, 1, 2], [3, 2, 1]]
    diagonal_secundaria_3 = matriz_expandida[[0, 1, 2], [4, 3, 2]]

    diagonais_secundarias = [diagonal_secundaria_1, diagonal_secundaria_2, diagonal_secundaria_3]

    # Calculando os produtos de cada diagonal

    produto_diagonais_principais = []

    for diagonal_principal in diagonais_principais:
        resultado = np.prod(diagonal_principal)
        produto_diagonais_principais.append(resultado)

    produto_diagonais_secundarias = []
    for diagonal_secundaria in diagonais_secundarias:
        resultado = np.prod(diagonal_secundaria)
        produto_diagonais_secundarias.append(resultado)

    determinante = sum(produto_diagonais_principais) - sum(produto_diagonais_secundarias)

    print(f"O determinante de sua matriz é {determinante}.")
    return determinante


calcular_determinante(matriz)







