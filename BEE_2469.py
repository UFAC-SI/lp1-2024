x = int(input())
frequencia = [0] * 101
#print(frequencia)
linha = input().split()
for i in range(len(linha)):
    nota = int(linha[i])
    frequencia[nota] += 1
#print(frequencia)
maior = 0
posicao = 0
for j in range(len(frequencia)):
    if maior <= frequencia[j]:
        posicao = j
        maior = frequencia[j]
print(posicao)