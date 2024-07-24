valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
maior_a_b = (a+b+abs(a-b))/2
maior = (maior_a_b+c+abs(maior_a_b-c))/2
#print(f'{maior:.0f} eh o maior')
print(f'{int(maior)} eh o maior')