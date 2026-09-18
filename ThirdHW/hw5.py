import numpy as np

m = int(input())
n = int(input())

matrix = np.zeros((m, n), dtype=int)

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            matrix[i, j] = i + j
    else:
        for j in range(n - 1, -1, -1):
            matrix[i, j] = i + j

matrix = matrix + 1

for i in range(m):
    matrix[i] += 10 * i
    matrix[i] = matrix[i] * i
print(matrix)

