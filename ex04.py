matriz1 = [
    [9,4,5],
    [3,8,2],
    [6,1,7]
]

matriz2 = [
    [3,1,2],
    [6,5,4],
    [8,2,9]
]

for l in range(0,3):
    for c in range(0,3):
        newMatrix = matriz1[l][c] - matriz2[l][c]
        print(f"[{newMatrix}]", end = '')
    print()