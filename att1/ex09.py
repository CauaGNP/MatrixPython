matrix1 =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for l in range(0,3):
    for c in range(0,3):
        k = 3
        newMatriz = matrix1[l][c] * k
        print(f"[{newMatriz}]", end = '')
    print()
