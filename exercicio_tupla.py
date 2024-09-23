#Entrada: (1,2,3) (4,5,6,7,8)
#Converter em uma lista
s1, s2 = input().split()
t1 = tuple(map(int, s1.replace('(','').replace(')','').split(',')))
t2 = tuple(map(int, s2.replace('(','').replace(')','').split(',')))

lista = []
if len(t1) <= len(t2):
    for i in range(len(t1)):
        lista.append(t1[i])
        lista.append(t2[i])
    for i in range(len(t1), len(t2)):
        lista.append(t2[i])
else:
    for i in range(len(t2)):
        lista.append(t2[i])
        lista.append(t1[i])
    for i in range(len(t1)):
        lista.append(t1[i])
print(tuple(lista))
