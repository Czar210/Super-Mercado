import sqlite3
from datetime import datetime


def mostra_tudo():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT nome, preco, supermercado, tipo, data_preco FROM produtos ORDER BY nome ASC")
    resultados = cursor.fetchall()

    for row in resultados:
        print(f"Nome: {row[0]}, Preço: {row[1]}, Supermercado: {row[2]}, Tipo: {row[3]}, Data do Preço: {row[4]}")

    conn.close()
    
    
mostra_tudo()