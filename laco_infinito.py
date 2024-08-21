senha_padrao = '123'
print('Digite uma senha:')
while True:
    senha_digitada = input()
    if senha_digitada != senha_padrao:
        print('Senha Incorreta, digite novamente...')
    else:
        break
print('Senha correta!!!')