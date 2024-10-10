matriz1 = [
    [4,9],
    [3,2],
]

matriz2 = [
    [1,5],
    [6,8]
]

for l in range(0,2):
    for c in range(0,2):
        newMatrix = matriz1[l][c] + matriz2[l][c]
        print(f"[{newMatrix}]", end = '')
    print()