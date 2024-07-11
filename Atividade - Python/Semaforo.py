import tkinter as tk

class SemafaroGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Semáforo")
        self.master.geometry("200x400")

        self.cor_vermelha = tk.Canvas(master, width=100, height=100, bg="black")
        self.cor_vermelha.create_oval(10, 10, 90, 90, fill="black")
        self.cor_vermelha.grid(row=0, column=0, padx=50, pady=10)
        
        self.cor_verde = tk.Canvas(master, width=100, height=100, bg="black")
        self.cor_verde.create_oval(10, 10, 90, 90, fill="green")
        self.cor_verde.grid(row=2, column=0, padx=50, pady=10)
        
        self.cor_amarela = tk.Canvas(master, width=100, height=100, bg="black")
        self.cor_amarela.create_oval(10, 10, 90, 90, fill="black")
        self.cor_amarela.grid(row=1, column=0, padx=50, pady=10)
        
        self.botao = tk.Button(master, text="Parar", command=self.parar_troca)
        self.botao.grid(row=3, column=0, pady=10)
        
        self.estado = 0
        self.intervalo = 2000  # Intervalo em milissegundos (2 segundos)
        self.trocar_luz()  # Começa a troca de luz automaticamente

    def trocar_luz(self):
        if self.estado == 0:
            self.cor_verde.itemconfig(1, fill="black")
            self.cor_amarela.itemconfig(1, fill="yellow")
            self.estado = 1
        elif self.estado == 1:
            self.cor_amarela.itemconfig(1, fill="black")
            self.cor_vermelha.itemconfig(1, fill="red")
            self.estado = 2
        else:
            self.cor_vermelha.itemconfig(1, fill="black")
            self.cor_verde.itemconfig(1, fill="green")
            self.estado = 0
        
        self.timer_id = self.master.after(self.intervalo, self.trocar_luz)  # Configura o temporizador novamente

    def parar_troca(self):
        if hasattr(self, 'timer_id'):
            self.master.after_cancel(self.timer_id)

def main():
    root = tk.Tk()
    semaforo_gui = SemafaroGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

