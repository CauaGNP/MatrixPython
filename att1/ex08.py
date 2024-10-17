matriz1 = [
    [2, 3, 1],  
    [4, 0, 5]   
]

matriz2 = [
    [1, 2],     
    [3, 4],     
    [5, 6]      
]

def multiplyMatrix(matrix1, matrix2):
    result = [[0, 0], [0, 0]]

    for l in range(len(matrix1)):
        for c in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[l][c] += matrix1[l][k] * matrix2[k][c]
    
    return result

result = multiplyMatrix(matriz1, matriz2)

for l in result:
    print(l)
