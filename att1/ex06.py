matriz1 = [
    [6,8],
    [4,7]
]

matriz2 = [
    [3,2],
    [5,1],
]

for l in range(0,2):
    for c in range(0,2):
        newMatrix = matriz1[l][c] - matriz2[l][c]
        print(f"[{newMatrix}]", end = '')
    print()