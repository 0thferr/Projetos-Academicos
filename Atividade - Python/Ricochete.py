import tkinter as tk

# Configurações da tela
TAMANHO_TELA = 600
VELOCIDADE_BOLA = 10

# Cores
COR_BOLA = "blue"
COR_PAREDE = "gray"

class Bola:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_oval(TAMANHO_TELA / 2, TAMANHO_TELA / 2, TAMANHO_TELA / 2 + 20, TAMANHO_TELA / 2 + 20, fill=COR_BOLA)
        self.velocidade_x = VELOCIDADE_BOLA
        self.velocidade_y = VELOCIDADE_BOLA

    def mover(self):
        self.canvas.move(self.shape, self.velocidade_x, self.velocidade_y)
        pos = self.canvas.coords(self.shape)
        if pos[2] >= TAMANHO_TELA or pos[0] <= 0:
            self.velocidade_x *= -1
        if pos[3] >= TAMANHO_TELA or pos[1] <= 0:
            self.velocidade_y *= -1

class Jogo:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=TAMANHO_TELA, height=TAMANHO_TELA, bg=COR_PAREDE)
        self.canvas.pack()

        self.botao_parada = tk.Button(root, text="Parar", command=self.parar_jogo)
        self.botao_parada.pack()

        self.botao_reset = tk.Button(root, text="Reset", command=self.reset_jogo)
        self.botao_reset.pack()

        self.jogando = True
        self.bola = Bola(self.canvas)
        self.mover_bola()

    def mover_bola(self):
        if self.jogando:
            self.bola.mover()
            self.root.after(50, self.mover_bola)

    def parar_jogo(self):
        self.jogando = False

    def reset_jogo(self):
        self.jogando = True
        self.canvas.delete(tk.ALL)  # Limpa o canvas
        self.bola = Bola(self.canvas)
        self.mover_bola()

def main():
    root = tk.Tk()
    root.title("Jogo de Bola")
    jogo = Jogo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
