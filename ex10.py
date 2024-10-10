matrix1 =[
    [2,1],
    [0,3],
]

for l in range(0,2):
    for c in range(0,2):
        k = 4
        newMatriz = matrix1[l][c] * k
        print(f"[{newMatriz}]", end = '')
    print()
