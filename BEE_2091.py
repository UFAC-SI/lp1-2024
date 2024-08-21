n = int(input())
while n!=0:
    linha = list(map(int, input().split()))
    pilha = []
    #entrada --> 1 3 4 3 1
    #input().split() --> '1','3','4','3','1'
    #map --> 1,3,4,3,1
    #list --> [1,3,4,3,1]
    for item in linha:
        if item in pilha:
            pilha.remove(item)
        else:
            pilha.append(item)
    print(pilha[0])
    n = int(input())
