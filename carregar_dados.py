import pandas as pd
import sqlite3

# Função para criar a tabela produtos
def criar_tabela():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            supermercado TEXT NOT NULL,
            categoria TEXT NOT NULL,
            data_preco TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para adicionar produto ao banco de dados
def adicionar_produto(nome, preco, supermercado, categoria, data_preco):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, preco, supermercado, categoria, data_preco)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, preco, supermercado, categoria, data_preco))

    conn.commit()
    conn.close()

# Criação da tabela produtos
criar_tabela()

# Caminho do arquivo Excel
file_path = 'Trabalho_daniel_final_atualizado2.xlsx'

# Carrega os dados do Excel
dados = pd.read_excel(file_path)

# Itera sobre as linhas do DataFrame e adiciona os produtos ao banco de dados
for index, row in dados.iterrows():
    if pd.notna(row['Nome']):
        adicionar_produto(row['Nome'], row['preco'], row['supermercado'], row['Categoria'], row['Data'])
        print(f"{row['Nome']} adicionado com sucesso!")
