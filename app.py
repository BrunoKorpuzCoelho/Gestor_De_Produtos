# -*- coding: utf-8 -*-
from tkinter import ttk, font
from tkinter import *
import sqlite3



class Produto:
        
        
    db = "C:\\Users\\KorpuZ\\Desktop\\Gestor Produtos\\database\\produtos.db"


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
        self.botao_adicionar = ttk.Button(frame, text = "Guardar Produto", command = self.add_produto)
        self.botao_adicionar.grid(row = 3, columnspan = 2, sticky = W + E)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlighthickness = 0, bd = 0, font=("Dancing Script", 11))
        style.configure("mystyle.Treeview.Heading", font = ("Algerian", 13, "bold"))
        style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky" : NSEW})])

        self.tabela = ttk.Treeview(height = 20, columns = 2, style = "mystyle.Treeview")
        self.tabela.grid(row = 4, column = 0, columnspan = 2)
        self.tabela.heading("#0", text = "Nome: ", anchor = CENTER)
        self.tabela.heading("#1", text = "Preço: ", anchor = CENTER)

        self.get_produtos()

    
    def db_consulta(self, consulta, parametros = ()):

        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit
        return resultado
    
    def get_produtos(self):

        registos_tabela = self.tabela.get_children()
        for linha in registos_tabela:
            self.tabela.delete(linha)
        query = "SELECT * FROM produto ORDER BY nome DESC"
        registos_db = self.db_consulta(query)
        for linha in registos_db:
            print(linha)
            self.tabela.insert("", 0, text = linha[1], values = linha[2])
        
    def validacao_nome(self):

        nome_introduzido_por_utilizador = self.nome.get()
        return len(nome_introduzido_por_utilizador) != 0
    
    def validacao_preco(self):

        preco_introduzido_por_utilizador = self.preco.get()
        return len(preco_introduzido_por_utilizador)
    
    def add_produto(self):

        if self.validacao_nome() and self.validacao_preco():
            query = "INSERT INTO produto VALUES(NULL, ?, ?)"
            parametros = (self.nome.get(), self.preco.get())
            self.db_consulta(query, parametros)
            print("Dados Guardados")

        
        if self.validacao_nome() and self.validacao_preco():
            print(self.nome.get())
            print(self.preco.get())
        elif self.validacao_nome() and not self.validacao_preco():
            print("O preço é obrigatório")
        elif not self.validacao_nome() and self.validacao_preco():
            print("O nome é obrigatório")
        else:
            print("O nome e o preço são obrigatórios")
        
        self.get_produtos()
        

            
    


        





if __name__ == "__main__":
    root = Tk()
    app = Produto(root)
    root.mainloop()



