matriz1 = [
    [3,5,7],
    [1,4,6],
    [9,2,8]]

matriz2 = [
    [6,3,1],
    [7,2,0],
    [5,8,4]
]

for l in range(0,3):
    for c in range(0,3):
        newMatrix = matriz1[l][c] + matriz2[l][c]
        print(f"[{newMatrix}]", end = '')
    print()