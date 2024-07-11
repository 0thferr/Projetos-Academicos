from tkinter import *
import turtle

# Define a tela
tela = turtle.Screen() #objeto da tela
tela.setup(width=800, height=600) #alterando o tamanho da tela 
tela.bgcolor('black') #cor de fundo da tela

# Cria a bola
bola = turtle.Turtle() #criando a bola a partir do turtle
bola.shape("circle") #definindo o circulo
bola.color("red") #definindo a cor
bola.penup() #"para" de desenhar
bola.setposition(0, -250) #vai para sua posicao inicial
bola.shapesize(2) #tamanho

# Define a função para lançar a bola
def lancar_bola():
  bola.setheading(90) #em qual direcao a "bola" esta apontando, no caso 90graus
  bola.showturtle() #mostrar tartaruga (ou mostrar lapis)
  while bola.ycor() < 300:  #bola.ycor retorna a coordenada y da bola. Enquanto for menor que 300 faz
    bola.forward(10) #move 10 unidades

def resetar_posicao_bola(): #metodo para resetar
    bola.hideturtle() #"esconde" a bola ou o lapis
    bola.speed(20)  #aumenta a velocidade
    bola.goto(0, -300) #leva a bola ao ponto inicial
    bola.setheading(90) #muda a direcao em que ela vai "olhar"

# Cria o botão para lançar a bola
botao_lancar = turtle.Turtle() #objeto do botao
botao_lancar.shape("square") #faz um quadrado
botao_lancar.color("green") #muda a cor do botao
botao_lancar.penup() #tira o "lapis"
botao_lancar.setposition(-250, 0) #posical inicial do botao


# Define a função para detectar o clique no botão
def clicar_botao(x, y): #recebe os parametros da coordenada onde o click ocorre
    #50 é um gap para o click permitindo essa margem  :  xcor() coordenada atual
  if botao_lancar.xcor() - 50 < x < botao_lancar.xcor() + 50 and botao_lancar.ycor() - 50 < y < botao_lancar.ycor() + 50: #verifica se as coordenadas do click do mouse estão dentro da area ao redor do botao. Comparacao da coorneada de click com a coordenada do botao
    #lancar_bola()
    for _ in range(50): #loop da bola na tela, lanca e volta, lanca e volta.
        lancar_bola()
        resetar_posicao_bola()

# Eventos de clique
tela.onclick(clicar_botao) #chama a função clicar botão a partir do lugar da tela em que o usuario clicou/ verifica se o clico ocorreu naquela area

# Inicia o loop principal
while True:
  # Atualiza a interface
  tela.update()