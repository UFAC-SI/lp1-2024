from functools import *
fatura = [('Net', 199.9),('Ifood', 999.87),('Gasolina', 678.0),('Formigão', 400)]
# Imprimir no formato ‘Tipo de gasto’ – R$ valor
# Ordenar os itens por valor
# Filtrar os gastos acima de R$ 500
# Apresentar o total da fatura

print('\n'.join(map(lambda x:f'{x[0]} - R${x[1]}', fatura)))
fatura.sort(key = lambda x:x[1],reverse=False)
print(fatura)
maiores = list(filter(lambda x:x[1]>500, fatura))
print(maiores)
total1 = reduce(lambda x,y: x + y[1], fatura, 0)
total2 = reduce(lambda x,y: x+y, list(dict(fatura).values()))
print(total1)
print(total2)