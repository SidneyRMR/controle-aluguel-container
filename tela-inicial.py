from itertools import count
import sqlite3
import pandas as pd
import tkinter as ttk
from tkinter import *

# Fazer coisa com o BD
#Criar uma conecção com o bd existente
conn = sqlite3.connect('clientes.db')# depois renomear para clientes novamente

#Criar uma instancia para o cursor
c = conn.cursor()

#Criar uma tabela
c.execute("""CREATE TABLE if not exists clientes (
    "nome"	TEXT NOT NULL,
    "sobrenome"	TEXT NOT NULL,
   	"rg"	TEXT NOT NULL,
   	"cpf"	TEXT NOT NULL,
   	"celular"	TEXT NOT NULL,
   	"email"	TEXT NOT NULL,
   	"ruaResidencia"	TEXT NOT NULL,
   	"numeroResidencia"	INTEGER NOT NULL,
   	"bairroResidencia"	TEXT NOT NULL,
   	"cidadeResidencia"	TEXT NOT NULL,
   	"ruaObra"	TEXT NOT NULL,
   	"numeroObra"	INTEGER NOT NULL,
   	"bairroObra"	TEXT NOT NULL,
   	"cidadeObra"	TEXT NOT NULL,
   	"referenciaObra"	TEXT NOT NULL,
   	PRIMARY KEY("rg")
    """)

#Commit mudanças
conn.commit()

#Fechar conexão
conn.close()


#Seletor de banco de dados
def query_database():
    #Criar uma conecção com o bd existente
    conn = sqlite3.connect('clientes.db')# depois renomear para clientes novamente

    #Criar uma instancia para o cursor
    c = conn.cursor()


    c.execute("SELECT * FROM clientes")
    records = c.fetchall()


    #Contador global
    global count
    count = 0

    # Adicionar dados na tela
    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count)
        else:
            my_tree.insert(parent='', index='end', iid=count)
        #increment counter
        count += 1


    #Commit mudanças
    conn.commit()
    #Fechar conexão
    conn.close()

root = Tk()
root.title("Controle de aluguel de container")
root.iconbitmap('C:\Users\sidne\Desktop\container.png')
root.geometry("1000x500")

#Adicionar estilo
style = ttk.Style()

#Pegar um tema
style.theme_use('default')

#Configurar cores do Treeview
style.configure("Treeview",
    background="D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="D3D3D3")

#Trocar cor selecionada
style.map('Treeview',
    background=[('selected', "#347083")])

#Criar uma Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

#Criar uma Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

#Criar a Treeview
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_frame)
my_tree.pack()

#Configurar o Srollbar
tree_scroll.config(command=my_tree.yview)

#Definir as colunas
my_tree['columns'] = ("Primeiro Nome", "Sobrenome", "RG", "Celular", "Rua da Entrega", "Número")

#Formatar as colunas
my_tree.column("#0",width=0, stretch=NO)
my_tree.column("Primeiro Nome",anchor=W, width=100)
my_tree.column("Sobrenome",anchor=W, width=160)
my_tree.column("RG",anchor=CENTER, width=100)
my_tree.column("Celular",anchor=CENTER, width=100)
my_tree.column("Rua da Entrega",anchor=CENTER, width=180)
my_tree.column("Número",anchor=CENTER, width=50)

# Criar cabeçarios
my_tree.heading("#0",text="", anchor=W)
my_tree.heading("Primeiro Nome",text="Primeiro Nome", anchor=W)
my_tree.heading("Sobrenome",text="Sobrenome", anchor=W)
my_tree.heading("RG",text="RG", anchor=CENTER)
my_tree.heading("Celular",text="Celular", anchor=CENTER)
my_tree.heading("Rua da Entrega",text="Rua da Entrega", anchor=CENTER)
my_tree.heading("Número",text="Número", anchor=CENTER)

##Select datas from db in list format
# data = [
#    [name, lastname, rg, phone number, address, number]
#    []
#    []
###]

# Criar linhas com cores alternadas
my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')



data_frame = LabelFrame(root, text="Gravando")
data_frame.pack(fill="x", expands="yes",padx=20)





my_tree.bind("<ButtonRelease-1>", select_record)

#coloca os dados do bd dentro da lista
query_database()

root.mainloop()
