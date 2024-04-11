import numpy as np


matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])


result_matrix = np.dot(matrix1, matrix2)
determinant=np.linalg.det(result_matrix)
print(determinant)
print(result_matrix)

matrix1=np.array([[4, 7, 1],
                   [2, 6, 3],
                   [5, 2, 8]])
#tersi
ters=np.linalg.inv(matrix1)
print(ters)
