import sqlite3
from datetime import datetime


def adicionar_produto(nome, preco, supermercado, tipo, data_preco):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, preco, supermercado, tipo, data_preco)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, preco, supermercado, tipo, data_preco))

    conn.commit()
    conn.close()
    

# Adicionar produtos de exemplo
adicionar_produto('Arroz', 5.99, 'Supermercado A', 'Grãos', '2024-06-24')
adicionar_produto('Arroz', 6.49, 'Supermercado B', 'Grãos', '2024-06-24')
adicionar_produto('Arroz', 5.79, 'Supermercado C', 'Grãos', '2024-06-24')
adicionar_produto('Feijão', 4.49, 'Supermercado A', 'Grãos', '2024-06-24')
adicionar_produto('Feijão', 4.99, 'Supermercado B', 'Grãos', '2024-06-24')

import pandas as pd

# Carrega os dados do Excel
file_path = 'C:/Users/cesar/Downloads/Supermercado/Trabalho_daniel_final_atualizado2.xlsx'
dados = pd.read_excel(file_path)

# Exibe as primeiras linhas do DataFrame para verificar se os dados foram carregados corretamente
print(dados[1])

