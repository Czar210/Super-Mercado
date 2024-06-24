import sqlite3
import streamlit as st
from datetime import datetime
import pandas as pd

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
            tipo TEXT NOT NULL,
            data_preco TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para adicionar produto ao banco de dados
def adicionar_produto(nome, preco, supermercado, tipo, data_preco):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, preco, supermercado, tipo, data_preco)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, preco, supermercado, tipo, data_preco))

    conn.commit()
    conn.close()

# Função para buscar produtos
def buscar_produtos(parte_do_nome='', ordenar_por='preco ASC', supermercado=None):
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    query = "SELECT nome, preco, supermercado, tipo, data_preco FROM produtos WHERE nome LIKE ?"
    params = ['%' + parte_do_nome + '%']
    
    if supermercado:
        query += " AND supermercado = ?"
        params.append(supermercado)
    
    query += f" ORDER BY {ordenar_por}"

    cursor.execute(query, params)
    resultados = cursor.fetchall()
    conn.close()

    return resultados

# Função para buscar supermercados distintos
def buscar_supermercados_distintos():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT DISTINCT supermercado FROM produtos")
    resultados = cursor.fetchall()
    conn.close()

    return [row[0] for row in resultados]

# Criação da tabela com a nova estrutura
criar_tabela()

# Interface Streamlit
st.set_page_config(page_title="POO DRAGÃO GUERREIRO Gestão de Produtos de Supermercados 🐼", layout="centered")

# Adicionar imagem no topo
st.image("https://cdn.ome.lt/EWlvzO0sMGgiSsy0CbNtIkyEJ1A=/1200x630/smart/extras/conteudos/kung_fu_panda.jpg", use_column_width=True)  # Substitua o URL pelo caminho da sua imagem

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🐼POO DRAGÃO GUERREIRO Gestão de Produtos de Supermercados 🛒</h1>", unsafe_allow_html=True)

# Busca de Produtos
st.markdown("<h2 style='color: #FF5722;'>🔍 Buscar Produtos</h2>", unsafe_allow_html=True)
parte_do_nome = st.text_input('Parte do Nome do Produto', placeholder="Digite parte do nome do produto")
ordenar_por = st.selectbox('Ordenar por', ['Preço Ascendente', 'Preço Descendente', 'Nome Ascendente', 'Nome Descendente'], index=0)
ordenar_opcoes = {
    'Preço Ascendente': 'preco ASC',
    'Preço Descendente': 'preco DESC',
    'Nome Ascendente': 'nome ASC',
    'Nome Descendente': 'nome DESC'
}
supermercado_opcoes = [None] + buscar_supermercados_distintos()
supermercado = st.selectbox('Supermercado', supermercado_opcoes)

if st.button('Buscar'):
    resultados = buscar_produtos(parte_do_nome, ordenar_opcoes[ordenar_por], supermercado)

    st.markdown("<h2 style='color: #FF5722;'>📋 Resultados</h2>", unsafe_allow_html=True)
    if resultados:
        df = pd.DataFrame(resultados, columns=['Nome', 'Preço', 'Supermercado', 'Tipo', 'Data do Preço'])
        st.dataframe(df)
    else:
        st.write("Nenhum produto encontrado. 😕")

# Adicionar Novo Produto em uma nova janela
if st.button('Adicionar Novo Produto'):
    with st.expander('Adicionar Novo Produto', expanded=True):
        st.markdown("<h2 style='color: #2196F3;'>🆕 Adicionar Novo Produto</h2>", unsafe_allow_html=True)
        nome = st.text_input('Nome do Produto')
        preco = st.number_input('Preço', format="%.2f")
        supermercado = st.text_input('Supermercado')
        tipo = st.text_input('Tipo do Produto')
        data_preco = st.date_input('Data do Preço', datetime.now())

        if st.button('Salvar Produto'):
            adicionar_produto(nome, preco, supermercado, tipo, data_preco.strftime('%Y-%m-%d'))
            st.success('Produto adicionado com sucesso! 🎉')

# Rodapé
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<footer style='text-align: center; color: #888;'>© 2024 POODRAGÃO GUERREIRO Gestão de Produtos de Supermercados 🛒</footer>", unsafe_allow_html=True)
