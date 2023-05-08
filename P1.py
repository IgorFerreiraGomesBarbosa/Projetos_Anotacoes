# Problema: Tempo_de_jogo.py

hinicial: int; hfinal: int; duracao: int

hinicial = int(input("Hora incial: "))
hfinal = int(input("Hora final: "))

if hinicial < hfinal:
    duracoa = hfinal - hinicial
else:
    duracao = 24 - (hinicial - hfinal)

print (f"O JOGO DUROU {duracao} HORA(S)")