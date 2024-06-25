import sqlite3

# Criar e conectar ao banco de dados SQLite
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

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
    
    
    
# Criação da tabela com a nova estrutura
criar_tabela()


