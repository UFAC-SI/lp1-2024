n = int(input())
i = 0 #variável contadora
soma = 0 #variável acumuladora
status = True #variável indicadora
while i < n:
    x = int(input())
    soma = soma + i
    i = i + 1
    if i == 5:
        status = True
print(soma)
print(status)
