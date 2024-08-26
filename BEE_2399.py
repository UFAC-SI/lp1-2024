n =  int(input())
vet = []
for i in range(n):
    vet.append(int(input()))
res = [0] * n
for i in range(n):
    res[i] += vet[i]
    if i > 0:
        res[i] += vet[i-1]
    if i < n-1:
        res[i] += vet[i+1]

for i in range(n):
    print(res[i])