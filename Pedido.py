import tkinter as tk
from tkinter import *
from tkinter import font, ttk, PhotoImage
from PIL import Image, ImageTk
import random

def open_small_window():
    small_window = tk.Toplevel(root)
    small_window.title("Opcao Invalida")
    small_window.geometry("300x120")
    
    smallFont = font.Font(family="Monaco", size=9, weight="bold")
    label = tk.Label(small_window, text="Esta opcão é inválida! Escolha a outra opcão!", font=smallFont, wraplength=170)
    label.pack(side="top", padx=0, pady=15)
    
    styleClose = ttk.Style()
    styleClose.configure('C.TButton', font =('Monaco', 10, 'bold'), borderwidth = '10')
    styleClose.map("C.TButton", foreground = [('active', 'gray')], background = [('active', 'red')])

    close_button = ttk.Button(small_window, text="Fechar", style="C.TButton", command=small_window.destroy)
    close_button.pack(side="bottom", padx=0, pady=10)

def change_main_window():
    main_label.config(text="Voce aceita continuar namorando comigo?") 
    sim_button.config(command=open_large_window)
    nao_button.bind("<Enter>", change_nao_button_position)

    imagem = Image.open("abelha.png") 
    imagem = imagem.resize((200, 200))
    imagem = ImageTk.PhotoImage(imagem)
    
    imagem_label.config(image=imagem)
    imagem_label.image = imagem

def open_large_window():
    large_window = tk.Toplevel(root)
    large_window.title("Meu Universo Todo!!!")
    large_window.geometry("500x500")

    frameCnt = 12
    frames = [PhotoImage(file='gif_heart.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
        
    label = Label(large_window)
    label.pack()
    root.after(0, update, 0)

    large_window1 = tk.Toplevel(root)
    large_window1.title("Meu Universo Todo!!!")
    large_window1.geometry("770x350")

    largeFont = font.Font(family="Monaco", size=15, weight="bold")
    label1 = tk.Label(large_window1, 
                    text="Gruda em mim\nQue eu quero te dar as estrelas desse céu azul anil\nSó pra compensar todas as vezes que você olhou pra mim e sorriu\nE aí\n\nPensa em mim\nMas pensa com carinho porque eu sei que vale à pena\nQue o nosso amor vai além de qualquer problema\nE aí\n\nMe pega pra você\nQue eu to me colocando bem na palma da tua mão\nQue eu to compartilhando a tempestade e o que há de bom\nEm mim",
                    font=largeFont, fg='black', wraplength=770, justify="left" )
    label1.pack(side="left", padx=0, pady=0)

def change_nao_button_position(event):
    x = random.randint(20, root.winfo_width() - 120)
    y = random.randint(20, root.winfo_height() - 50)
    nao_button.place(x=x, y=y)
    nao_button.lift()

root = tk.Tk()
root.title("Um pedido especial")
root.geometry("800x600")
cor_fundo = "#FFC0CB" 
root.configure(bg=cor_fundo)

main_label = tk.Label(root, text="Amor, voce gostaria de seguir em frente com esse pedido?")
text_init = "Amor, voce gostaria de seguir em frente com esse pedido?"
estilo_fonte = font.Font(family="Monaco", size=20, weight="bold")
main_label = tk.Label(text=text_init, bg=cor_fundo, font=estilo_fonte, fg="#8b0000", wraplength=600)
main_label.pack(side="top", padx=0, pady=120)

styleSim = ttk.Style()
styleSim.configure('S.TButton', font =('Monaco', 20, 'bold'),borderwidth = '10')
styleSim.map("S.TButton", foreground = [('active', 'green')], background = [('active', 'black')])
sim_button = ttk.Button(text="Sim", style="S.TButton", command=change_main_window)
sim_button.pack(side="left", padx=100, pady=0)

styleSim = ttk.Style()
styleSim.configure('N.TButton', font =('Monaco', 20, 'bold'), borderwidth = '10')
styleSim.map("N.TButton", foreground = [('active', 'red')], background = [('active', 'black')])
nao_button = ttk.Button(text="Não", style="N.TButton", command=open_small_window)
nao_button.pack(side="right", padx=100, pady=0)

imagem_vazia = Image.new("RGB", (200, 200), cor_fundo)
imagem_vazia = ImageTk.PhotoImage(imagem_vazia)
global imagem_label
imagem_label = tk.Label(image=imagem_vazia, bg=cor_fundo)
imagem_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()