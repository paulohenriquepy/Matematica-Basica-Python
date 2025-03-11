import numpy as np

# Função para calcular o determinante de uma matriz 3x3

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

first_column = data[0:3, 0]
second_column = data[0:3, 1]

new_data = np.column_stack( (data,first_column) )
final_data = np.column_stack( (new_data,second_column) )

print(final_data)

diagonal_principal_1 = final_data[[0, 1, 2], [0, 1, 2]]
diagonal_principal_2 = final_data[[0, 1, 2], [1, 2, 3]]
diagonal_principal_3 = final_data[[0, 1, 2], [2, 3, 4]]

diagonal_secundaria_1 = final_data[[0, 1, 2], [2, 1, 0]]
diagonal_secundaria_2 = final_data[[0, 1, 2], [3, 2, 1]]
diagonal_secundaria_3 = final_data[[0, 1, 2], [4, 3, 2]]

print(diagonal_principal_1)

# Calculando os produtos de cada diagonal

produto_dp1 = np.prod(diagonal_principal_1)
print(produto_dp1)


