from customtkinter import *
import random

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("645x316")
        self.text()
        self.input()
        self.button()
        self.sair()
        self.numero_aleatorio = random.randint(1, 15)  # Gera um número aleatório
        self.tentativas = 0
        self.erros = 0

    def text(self):
        self.label = CTkLabel(master=self.master, text="Bem-vindo ao jogo 'Chute o número'! Tente adivinhar o número que estou pensando, que está entre 1 e 15.", font=("Jockey one", 15))
        self.label.place(x=30, y=10)

    def input(self):
        self.ent = CTkEntry(master=self.master, placeholder_text="Chute o número", width=90, font=("Jockey one", 15), justify='center')  
        self.ent.place(x=279, y=45)

    def button(self):
        btn = CTkButton(master=self.master, text="Chute o número", corner_radius=58, fg_color="#4D5D89",
                hover_color="#374D85", border_color="#000000",
                border_width=1, command=self.verificar_chute)
        btn.place(x=175, y=80)
    
    def sair(self):
        sair = CTkButton(master=self.master, text="Sair", corner_radius=58, fg_color="#4D5D89",
                hover_color="#374D85", border_color="#000000",
                border_width=1, command=self.master.destroy)
        sair.place(x=330, y=80)

    def verificar_chute(self):
        try:
            chute = int(self.ent.get())  # Obtém o chute do Entry
            
            if chute < 1 or chute > 15:
                self.mostrar_mensagem("Por favor, insira um número válido entre 1 e 15.", 180)
                return
            
            self.tentativas += 1

            if chute < self.numero_aleatorio:
                self.mostrar_mensagem(f"Tente um número maior. Tentativas incorretas: {self.erros}", 210)
                self.erros += 1
            elif chute > self.numero_aleatorio:
                self.mostrar_mensagem(f"Tente um número menor. Tentativas incorretas: {self.erros}", 210)
                self.erros += 1
            else:
                self.parabens()

        except ValueError:
            self.mostrar_mensagem("Entrada inválida. Por favor, insira um número válido.", 180)

    def parabens(self):
        label = CTkLabel(master=self.master, text="Parabéns! Você acertou o número.", font=("Jockey one", 15))
        label.place(x=230, y=120)
        self.mostrar_acerto()

    def mostrar_acerto(self):
        label = CTkLabel(master=self.master, text=f"O número correto era {self.numero_aleatorio}. Você fez {self.tentativas} tentativas.", font=("Jockey one", 15))
        label.place(x=120, y=145)

    def mostrar_mensagem(self, mensagem, y):
        # Remova a mensagem anterior antes de exibir a nova
        for widget in self.master.winfo_children():
            if isinstance(widget, CTkLabel) and widget != self.label:
                widget.destroy()
                
        label = CTkLabel(master=self.master, text=mensagem, font=("Jockey one", 15))
        label.place(x=180, y=y)

app = CTk()
start = App(app)
app.mainloop()
