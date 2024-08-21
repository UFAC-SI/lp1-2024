dia_entrada = input().split()
dia_inicio = int(dia_entrada[1])
tempo_entrada = input().split(" : ")
hora_inicio = int(tempo_entrada[0])
minuto_inicio = int(tempo_entrada[1])
segundo_inicio = int(tempo_entrada[2])
dia2_entrada = input().split()
dia_fim = int(dia2_entrada[1])
tempo2_entrada = input().split(" : ")
hora_fim = int(tempo2_entrada[0])
minuto_fim = int(tempo2_entrada[1])
segundo_fim = int(tempo2_entrada[2])

inicio = (dia_inicio * 86400 + hora_inicio * 3600 + minuto_inicio * 60 +
          segundo_inicio)
fim = dia_fim * 86400 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim

diff = fim - inicio
dia = diff // 86400
diff = diff % 86400
hora = diff // 3600
diff = diff % 3600
minuto = diff // 60
segundo = diff % 60

print(f'{dia} dia(s)')
print(f'{hora} hora(s)')
print(f'{minuto} minuto(s)')
print(f'{segundo} segundo(s)')
#Exemplo de entrada
# Dia 5
# 08 : 01 : 00
# Dia 5
# 08 : 02 : 01


