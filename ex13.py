import locale

mat1 = []
mat2 = []
matsoma = []

for _ in range(3):
    mat1.append([0] * 3)

for _ in range(3):
    mat2.append([0] * 3)

for _ in range(3):
    matsoma.append([0] * 3)

print("PRIMEIRA MATRIZ")
for l in range(3):
    for c in range(3):
        mat1[l][c] = int(input(f"informe a posição da linha {l}, e da coluna {c} da matriz.\n"))

print("SEGUNDA MATRIZ")
for l in range(3):
    for c in range(3):
        mat2[l][c] = int(input(f"informe a posição da linha {l}, e da coluna {c} da matriz.\n"))

for l in range(3):
    for c in range(3):
        matsoma[l][c] = mat1[l][c] + mat2[l][c]

print("SOMA DAS 2 MATRIZES")
for l in range(3):
    for c in range(3):
        print(f"| {matsoma[l][c]} |", end="")
    print()
    
#somandomatrizes2
