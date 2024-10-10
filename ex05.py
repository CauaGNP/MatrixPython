matriz1 = [
    [7,9,2],
    [4,5,6]
]

matriz2 = [
    [2,3,5],
    [8,7,1]
]

for l in range(0,2):
    for c in range(0,3):
        newMatrix = matriz1[l][c] - matriz2[l][c]
        print(f"[{newMatrix}]", end = '')
    print()