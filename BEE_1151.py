# 0 1 1 2 3 5
n = int(input())
ant = 0; prox = 1
if n < 2:
    print(ant)
else:
    print(ant, prox, end=' ')
    for i in range(1,n-2):
        aux = ant
        ant = prox
        prox = aux + ant
        print(prox, end=' ')
    print(ant+prox)