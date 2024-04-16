import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "bd.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_table(conexao,cursor):
    cursor.execute(" CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(60), email VARCHAR(60))")
    conexao.commit()
    
def inserir_registros(conexao,cursor,nome,email):
    cursor.execute(f" INSERT INTO clientes (nome,email) VALUES('{nome}','{email}')")
    conexao.commit()
    print("Dados Registrados com sucesso...")

def atulizar_registros(conexao,cursor,id,nome,email):
    
    data =[nome,email,id]
    cursor.execute(f" UPDATE clientes SET nome=?,email=? WHERE id=?;",data)
    conexao.commit()
    print("Dados Atualizados com sucesso...")

def listar_dados(cursor):
    cursor.execute("SELECT * FROM clientes")
    #fetchone()
    regs = cursor.fetchall()
    for row in regs:
        print(dict(row))

def excluir_registros(conexao,cursor,id):
    
    data =(id,)
    cursor.execute(f" DELETE FROM clientes  WHERE id=?;",data)
    conexao.commit()
    print("Registro Excluido com sucesso...")

def inserir_lote(conexao,cursor,regs):

    cursor.executemany(f" INSERT INTO clientes (nome,email) VALUES(?,?)",regs)
    conexao.commit()

    
#criar_table(conexao,cursor)
#inserir_registros(conexao,cursor,"Alvinho","alvinho@python.com")
#atulizar_registros(conexao,cursor,"Alvinho Soares","alvinho@python.me",1)
#excluir_registros(conexao,cursor,1)
listar_dados(cursor)
regs=[
    ("Carla","carla@gmail.com"),
    ("Carlos","carlos@gmail.com"),
    ("ana","ana@gmail.com"),
    ("pedro","pedro@gmail.com"),

]
#inserir_lote(conexao,cursor,regs)