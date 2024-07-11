'''
200011514 Thais Ferreira
'''
valor = list(range(4))
for i in range(4):
    valor[i] = (int(input("Comece com o %dº valor:"%(i+1))))
if valor[0] >= valor[1] and valor[0] >= valor[2] and valor[0] >= valor[3]:
    print ("O 1º valor é Maior")
elif valor[1] >= valor[2] and valor[1] >= valor[3]:
    print ("O 2º valor é Maior")
elif valor[2] >= valor[3]:
    print ("O 3º valor é Maior")
else:
    print("O 4º valor é Maior")