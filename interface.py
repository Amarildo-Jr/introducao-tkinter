from tkinter import *

def somar():
    num1 = int (entrada.get())
    num2 = int (entrada2.get())
    resultado.config(text=f"A soma entre {num1} e {num2} resulta em {num1 + num2}.")

def subtrair():
    num1 = int (entrada.get())
    num2 = int (entrada2.get())
    resultado.config(text=f"A diferença entre {num1} e {num2} resulta em {num1 - num2}.")

def alternar_soma():
    btn_somar.config(text="Somar", command=somar)
    resultado.config(text="")

def alternar_subtracao():
    btn_somar.config(text="Subtrair", command=subtrair)
    resultado.config(text="")

janela = Tk()
janela.title("Interface em Python")
janela.geometry("600x400")

menu_principal = Menu(janela)
janela.config(menu=menu_principal)

menu_operacoes = Menu(menu_principal)
menu_principal.add_cascade(label="Operações", menu=menu_operacoes)

menu_operacoes.add_command(label="Soma", command=alternar_soma)
menu_operacoes.add_command(label="Subtracao", command=alternar_subtracao)


legenda = Label(janela, text="Digite um numero")
legenda.pack()
entrada = Entry(janela)
entrada.pack()

legenda2 = Label(janela, text="Digite outro numero")
legenda2.pack()
entrada2 = Entry(janela)
entrada2.pack()

btn_somar = Button(janela, text="Somar", command=somar)
btn_somar.pack()

resultado = Label(janela, text="")
resultado.pack()

janela.mainloop()