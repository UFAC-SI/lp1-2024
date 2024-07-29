valor = int(input())
#if valor > 10 and valor < 20:
if 0 < valor < 10:
    print(f'{valor} está entre 0 e 10')
elif 10 < valor < 20:
    print(f'{valor} está entre 10 e 20')
elif 20 < valor < 30:
    print(f'{valor} está entre 20 e 30')
else:
    print(f'{valor} está fora do intervalo')
# Operador ternário
#s = f'{valor} está entre 10 e 20' if 10 < valor < 20 else 'fora'
#print(s)