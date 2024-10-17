matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [2, 0],
    [1, 3]
]

def multiplyMatrix(matrix1, matrix2):
    result = [[0, 0], [0, 0]]

    for l in range(len(matrix1)):
        for c in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[l][c] += matrix1[l][k] * matrix2[k][c]
    
    return result

result = multiplyMatrix(matriz1, matriz2)

for linha in result:
    print(linha)