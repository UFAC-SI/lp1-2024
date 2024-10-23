try:
    x = int(input())
    #o comando assert é usado para testar uma expressão
    #e gera uma exceção caso o valor seja False
    #Exemplo de teste
    #assert x >= 0, 'O valor não pode ser negativo'
    #Exemplo de tratamento de exceção
    if x < 0:
        raise ValueError('O valor não pode ser negativo, com tratamento de exceção.')
    print(x)
except AssertionError as ase:
    print(str(ase))
except ValueError as vae:
    print(str(vae))