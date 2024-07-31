n = int(input())
i = 0 #variável contadora
status = True #variável indicadora
ant = int(input())
while i < n-1:
    x = int(input())
    if x < ant:
        status = False
    i = i + 1
    ant = x
if status == True:
    print('crescente')
else:
    print('não crescente')