senha_padrao = '123'
print('Digite uma senha:')
while True:
    try:
        senha_digitada = input()
        if senha_digitada != senha_padrao:
            print('Senha Incorreta, digite novamente...')
        else:
            print('Senha correta!!!')
    except EOFError:
        break
