import sqlite3
import tkinter as tk
from tkinter import ttk
from turtle import width
import pandas as pd

#Criando Janela:

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela. geometry("1000x800")

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:rg,:cpf,:email,:celular,:ruaResidencia,:numeroResidencia,:bairroResidencia,:cidadeResidencia,:ruaObra,:numeroObra,:bairroObra,:cidadeObra,:referenciaObra)",
              {
	                "nome":	entry_nome.get(),
	                "sobrenome":	entry_sobrenome.get(),
                  "rg":	entry_rg.get(),
    	            "cpf":	entry_cpf.get(),
    	            "celular":	entry_telefone.get(),
    	            "email":	entry_email.get(),
    	            "ruaResidencia":	entry_ruaResidencia.get(),
    	            "numeroResidencia":	entry_numeroResidencia.get(),
    	            "bairroResidencia":	entry_bairroResidencia.get(),
    	            "cidadeResidencia":	entry_cidadeResidencia.get(),
    	            "ruaObra":	entry_ruaObra.get(),
    	            "numeroObra":	entry_numeroObra.get(),
    	            "bairroObra":	entry_bairroObra.get(),
    	            "cidadeObra":	entry_cidadeObra.get(),
    	            "referenciaObra":	entry_referenciaObra.get(),
              })
    # Commit as mudanças:
    conexao.commit()
    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_rg.delete(0,"end")
    entry_cpf.delete(0,"end")
    entry_telefone.delete(0,"end")
    entry_email.delete(0,"end")
    entry_ruaResidencia.delete(0,"end")
    entry_numeroResidencia.delete(0,"end")
    entry_bairroResidencia.delete(0,"end")
    entry_cidadeResidencia.delete(0,"end")
    entry_ruaObra.delete(0,"end")
    entry_numeroObra.delete(0,"end")
    entry_bairroObra.delete(0,"end")
    entry_cidadeObra.delete(0,"end")
    entry_referenciaObra.delete(0,"end")


# Botão exportar para excel
# def exporta_clientes():
#     conexao = sqlite3.connect('clientes.db')
#     c = conexao.cursor()

#     # Inserir dados na tabela:
#     c.execute("SELECT *, oid FROM clientes")
#     clientes_cadastrados = c.fetchall()
#     # print(clientes_cadastrados)
#     clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['nome','sobrenome','rg','cpf','email','celular','ruaResidencia''numeroResidencia','bairroResidencia','cidadeResidencia','ruaObra','numeroObra','bairroObra','cidadeObra','referenciaObra''Id_banco'])
#     clientes_cadastrados.to_excel('clientes.xlsx')
#     # Commit as mudanças:
#     conexao.commit()
#     # Fechar o banco de dados:
#     conexao.close()


#Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=0, column=3, padx=10, pady=10)
entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=0, column=4, padx=10, pady=10)

label_rg = tk.Label(janela, text='RG')
label_rg.grid(row=1, column=0 , padx=10, pady=10)
entry_rg = tk.Entry(janela, width =35)
entry_rg.grid(row=1, column=1 , padx=10, pady=10)

label_cpf = tk.Label(janela, text='CPF')
label_cpf.grid(row=1, column=3, padx=10, pady=10)
entry_cpf = tk.Entry(janela, width =35)
entry_cpf.grid(row=1, column=4, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=2, column=3, padx=10, pady=10)
entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=2, column=4, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0 , padx=10, pady=10)
entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

##frame Endereço residencial
label_ruaResidencia = tk.Label(janela, text='Endereço residêncial')
label_ruaResidencia.grid(row=3, column=1,columnspan=1 , padx=10, pady=10)

label_ruaResidencia = tk.Label(janela, text='Rua residência')
label_ruaResidencia.grid(row=4, column=0 , padx=10, pady=10)
entry_ruaResidencia = tk.Entry(janela, width =35)
entry_ruaResidencia.grid(row=4, column=1 , padx=10, pady=10)

label_numeroResidencia = tk.Label(janela, text='Número')
label_numeroResidencia.grid(row=4, column=3 , padx=10, pady=10)
entry_numeroResidencia = tk.Entry(janela, width =35)
entry_numeroResidencia.grid(row=4, column=4 , padx=10, pady=10)

label_bairroResidencia = tk.Label(janela, text='Bairro')
label_bairroResidencia.grid(row=5, column=0 , padx=10, pady=10)
entry_bairroResidencia = tk.Entry(janela, width =35)
entry_bairroResidencia.grid(row=5, column=1 , padx=10, pady=10)

label_cidadeResidencia = tk.Label(janela, text='Cidade')
label_cidadeResidencia.grid(row=5, column=3 , padx=10, pady=10)
entry_cidadeResidencia = tk.Entry(janela, width =35)
entry_cidadeResidencia.grid(row=5, column=4 , padx=10, pady=10)

##frame Endereço para entrega
label_ruaResidencia = tk.Label(janela, text='Endereço para entrega')
label_ruaResidencia.grid(row=6, column=1, columnspan=1, padx=10, pady=10)

label_ruaObra = tk.Label(janela, text='Rua da entrega')
label_ruaObra.grid(row=7, column=0 , padx=10, pady=10)
entry_ruaObra = tk.Entry(janela, width =35)
entry_ruaObra.grid(row=7, column=1 , padx=10, pady=10)

label_numeroObra = tk.Label(janela, text='Número')
label_numeroObra.grid(row=7, column=3 , padx=10, pady=10)
entry_numeroObra = tk.Entry(janela, width =35)
entry_numeroObra.grid(row=7, column=4 , padx=10, pady=10)

label_bairroObra = tk.Label(janela, text='Bairro')
label_bairroObra.grid(row=8, column=0 , padx=10, pady=10)
entry_bairroObra = tk.Entry(janela, width =35)
entry_bairroObra.grid(row=8, column=1 , padx=10, pady=10)

label_cidadeObra = tk.Label(janela, text='Cidade')
label_cidadeObra.grid(row=8, column=3 , padx=10, pady=10)
entry_cidadeObra = tk.Entry(janela, width =35)
entry_cidadeObra.grid(row=8, column=4 , padx=10, pady=10)

label_referenciaObra = tk.Label(janela, text='Ponto de referência')
label_referenciaObra.grid(row=9, column= 0, padx=10, pady=10)
entry_referenciaObra = tk.Entry(janela, width =35)
entry_referenciaObra.grid(row=9, column=1, padx=10, pady=10)


# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=9, column=3,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

#botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
#botao_exportar.grid(row=8, column=3,columnspan=4, padx=10, pady=10 , ipadx = 80)


janela.mainloop()