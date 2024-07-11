import turtle as t
from random import randint
import tkinter as tk
from tkinter import *

def curve(): 
    for i in range(200):  #avança uma pequena distancia a cada iteração, fazendo uma curva gradual
        t.right(1) #1 grau para direita a cada iteração
        t.forward(1) # 1 para frente

def head():
    #fazendo o coração
    t.color('red') #a tartaruga desenhará com essa cor 
    t.begin_fill() #começo para preenchimento da cor. para no end_fill
    t.left(140) #girando a tartaruga
    t.forward(120) #movendo a tartaruga em linha reta
    curve() #faz a curva do coracao
    t.left(125) #gira a tartaruga novamente
    curve() #outra curva do coracao 
    t.forward(120) #novamente uma linha reta
    t.end_fill() #termina "Colorindo" o coração"

def points(x, y, size):
    t.penup() #metodo para a tartaruga se mover sem desenhar
    t.goto(x, y) #move a tartaruga para recomeçar o desenho
    t.pendown() #começa a desenhar novamente
    t.dot(size) #desenha um ponto com o tamanho como parametro.

def start_animation():
    draw() #começa a desenhar

def stop_animation():
    t.bye() #função para fechar a janela da animação

def draw():
    t.bgcolor('black') #tela de fundo preta
    t.shape('turtle') #coloca a forma da ponta como tartaruga, por padrão nao vem como tartaruga, vem uma seta
    head() #chama funcao para começar o desenho
    

    #fazendo a flecha no coracao
    t.penup() #usado para parar de desenhar e se mover
    t.goto(150, 150) #movendo a tartarug
    t.pensize(10) # tamanho da linha que vai desenhar
    t.hideturtle() #tartaruguinha some
    t.color('red2') #define cor
    t.pendown() #começa a desenhar
    t.goto(30, 110) #coordenadas
    t.penup() #para de desenhar
    t.goto(-60, 50) # vai para coordenadas
    t.pendown() #começa a desenhar
    t.goto(-115, 15) #move as coordenadas
    
    #gotas de coração
    for _ in range(20): #loop 20 gotas
        x = randint(-10, 12) #numero aleatorio para coordenadas á x
        y = randint(-150, -5) #numero aleatorio para y
        size = randint(2, 20) #tamanho das gotas aleatorio
        points(x, y, size) #desenhando os pontos com coordenadas e tamanho aleatorio (dentro de um limite) no fim do desenho

    t.exitonclick() #sair

def create_buttons():
    window = tk.Tk() #definindo a janela
    window.title("Tartaruguinha") #titulo da janela
    window.geometry("450x250") # tamanho da janela
    window.configure(background="#251002123") #cor de fundo 
    window.resizable(False, False) #nao pode ser mudado o tamanho


    label = tk.Label(window, text="Tartaruga Artística Super Criativa 5.0", font=("Arial", 15), bg="#251002123", fg="#fffffffff").place(x=55, y=20) #criando o texto e definindo suas particularidades


    start_button = tk.Button(window, text="Começar a obra artística!", command=start_animation, bg="#251002123", fg="#fffffffff") #criando botao e definindo suas particularidades
    start_button.pack(side=tk.LEFT, padx=50) #posicionando o botao
    stop_button = tk.Button(window, text="Parar Imediatamente!", command=stop_animation,  bg="#251002123", fg="#fffffffff")
    stop_button.pack(side=tk.LEFT, padx=20)
    
    window.mainloop() #loop para manter aberta ate o usuario fechar a janela :D

# Iniciar a criação dos botões em uma thread separada
create_buttons()
