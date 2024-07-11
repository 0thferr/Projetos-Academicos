import numpy as np
import random

def validaNum(coordenada):
    if coordenada < 0:
        coordenada = 0
    elif coordenada > tamanho-1:
        coordenada = tamanho-1
    return coordenada

def verificaMaior(coord1, coord2, coord3) :
    Maior_Redor_Valor =  menor-1
    global posicao
    global somatoria
    global notas
    global passos
    cubo[posicao[0]][posicao[1]][posicao[2]] = menor-1
    if (passos <= 300):
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if cubo[validaNum(coord1+i)][validaNum(coord2+j)][validaNum(coord3+k)] > Maior_Redor_Valor:
                        Maior_Redor_Valor = cubo[validaNum(coord1+i)][validaNum(coord2+j)][validaNum(coord3+k)]
                        Maior_Redor_Posicao = (validaNum(coord1+i), validaNum(coord2+j), validaNum(coord3+k))
    somatoria += Maior_Redor_Valor
    posicao = Maior_Redor_Posicao
    notas.write(f"Posição do passo {passos}: ({posicao[0]}, {posicao[1]}, {posicao[2]})\n")
    
    

passos = 0
tamanho = 10
menor = -100
maior = 100
somatoria = 0
cubo = np.random.randint(menor, maior+1, size= (tamanho, tamanho, tamanho))

# Define posição inicial
x = random.randint(0, tamanho-1)
y = random.randint(0, tamanho-1)
z = random.randint(0, tamanho-1)
posicao_inical = (x, y, z)
posicao = (x, y, z)
posicao_final = (random.randint(0, tamanho-1), random.randint(0, tamanho-1), random.randint(0, tamanho-1))
notas = open("Passos.txt", "w")
while True:
    passos += 1
    verificaMaior(posicao[0], posicao[1], posicao[2])
    print(f"Passo {passos}")
    if passos >= 300 or posicao == posicao_final:
        break
    

# Imprimir resultados
print(f"Posição inicial: ({posicao_inical[0]}, {posicao_inical[1]}, {posicao_inical[2]})")
print(f"Passos finais: {passos}")
print(f"Posição encerrada: ({posicao[0]}, {posicao[1]}, {posicao[2]})")
print(f"Posição final: ({posicao_final[0]}, {posicao_final[1]}, {posicao_final[2]})")
print(f"Somatória dos números coletados: {somatoria}")

notas.write(f"Posição inicial: ({posicao_inical[0]}, {posicao_inical[1]}, {posicao_inical[2]})\n")
notas.write(f"Passos finais: {passos}\n")
notas.write(f"Posição encerrada: ({posicao[0]}, {posicao[1]}, {posicao[2]})\n")
notas.write(f"Posição final: ({posicao_final[0]}, {posicao_final[1]}, {posicao_final[2]})\n")
notas.write(f"Somatória dos números coletados: {somatoria}\n")
