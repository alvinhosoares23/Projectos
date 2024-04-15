import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "bd.sqlite")
cursor = conexao.cursor()
nome = "Alvinho"
email = "alvinho@python.com"
cursor.execute(" CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(60), email VARCHAR(60))")
cursor.execute(f" INSERT INTO clientes (nome,email) VALUES('{nome}','{email}')")
conexao.commit()


