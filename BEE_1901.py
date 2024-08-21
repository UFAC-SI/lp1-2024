n = int(input())
matriz = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)
visitas =[]
for v in range(n*2):
    i, j = map(int, input().split())
    if matriz[i-1][j-1] not in visitas:
        visitas.append(matriz[i-1][j-1])
print(len(visitas))