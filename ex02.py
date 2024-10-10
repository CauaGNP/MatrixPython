matriz1 = [
    [2,3,4],
    [5,6,7],
]

matriz2 = [
    [8,7,6],
    [5,4,3]
]


for l in range(0,2):
    for c in range(0,3):
        newMatrix = matriz1[l][c] + matriz2[l][c]
        print(f"[{newMatrix}]", end = '')
    print()