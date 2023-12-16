from tkinter import ttk, font
from tkinter import *
import sqlite3



class Produto:

    def __init__(self, root):
        self.janela = root
        self.janela.title("App Gestor de Produtos")
        self.janela.resizable(1,1)
        self.janela.wm_iconbitmap("C:\\Users\\KorpuZ\\Desktop\\Gestor Produtos\\recursos\\icon.ico.ico")
        frame = LabelFrame(self.janela, text = "Registar um novo Produto")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        self.etiqueta_nome = Label(frame, text = "Nome: ")
        self.etiqueta_nome.grid(row = 1, column = 0)
        self.nome = Entry(frame)
        self.nome.focus()
        self.nome.grid(row = 1, column = 1)

        self.etiqueta_preco = Label(frame, text = "Preço: ")
        self.etiqueta_preco.grid(row = 2, column = 0)
        self.preco = Entry(frame)
        self.preco.grid(row = 2, column = 1)

        self.botao_adicionar = ttk.Button(frame, text = "Guardar Produto")
        self.botao_adicionar.grid(row = 3, columnspan = 2, sticky = W + E)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlighthickness = 0, bd = 0, font=("Dancing Script", 11))
        style.configure("mystyle.Treeview.Heading", font = ("Algerian", 13, "bold"))
        style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky" : NSEW})])

        self.tabela = ttk.Treeview(height = 20, columns = 2, style = "mystyle.Treeview")
        self.tabela.grid(row = 4, column = 0, columnspan = 2)
        self.tabela.heading("#0", text = "Nome: ", anchor = CENTER)
        self.tabela.heading("#1", text = "Preço: ", anchor = CENTER)

        





if __name__ == "__main__":
    root = Tk()
    app = Produto(root)
    root.mainloop()



