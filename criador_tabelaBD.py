import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
    CREATE TABLE "clientes" (
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
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()