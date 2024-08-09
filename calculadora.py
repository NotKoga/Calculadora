import tkinter as tk
from tkinter import messagebox


def adicionar():
    try:
        resultado.set(float(entrada1.get()) + float(entrada2.get()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números validos")

def subtrair():
    try:
        resultado.set(float(entrada1.get()) - float(entrada2.get()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números validos")

def multiplicar():
    try:
        resultado.set(float(entrada1.get()) * float(entrada2.get()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números validos")

def dividir():
    try:
        if float(entrada2.get()) == 0:
            raise ZeroDivisionError
        resultado.set(float(entrada1.get()) / float(entrada2.get()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números validos")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por 0(zero) não é permitida")



root = tk.Tk()
root.title("Calculadora de ganhos do Tigrinho")

root.configure(bg='#784c7d')

entrada1 = tk.StringVar()
entrada2 = tk.StringVar()
resultado = tk.StringVar()

tk.Label(root,text="Primeiro n°: ").grid(row=0, column=0)
tk.Entry(root, textvariable=entrada1).grid(row=0, column=1)

tk.Label(root,text="Segundo n°: ").grid(row=1, column=0)
tk.Entry(root, textvariable=entrada2).grid(row=1, column=1)

button_style = {
    'font': ('Arial', 16),
    'bg': '#9b6d9e',
    'fg': '#ffffff',
    'relief': 'ridge',
    'bd': 2,
    'width': 1,
    'height': 1

}

tk.Button(root, text="+", command=adicionar, **button_style).grid(row=0, column=3)
tk.Button(root, text="-", command=subtrair, **button_style).grid(row=0, column=4)
tk.Button(root, text="x", command=multiplicar, **button_style).grid(row=1, column=3)
tk.Button(root, text=":", command=dividir, **button_style).grid(row=1, column=4)

tk.Label(root, text="Resultado: ").grid(row=3, column=0)
tk.Entry(root, textvariable=resultado, state='readonly').grid(row=3, column=1)

root.mainloop()