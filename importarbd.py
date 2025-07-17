import sqlite3
import pandas as pd

# Criar conexão com banco de dados SQLite em memória (pode ser exportado depois)
conn = sqlite3.connect('data/vendas_loja.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT,
    cidade TEXT
)
''')

cursor.execute('''
CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL
)
''')

cursor.execute('''
CREATE TABLE vendas (
    id_venda INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_produto INTEGER,
    data TEXT,
    quantidade INTEGER,
    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
)
''')

# Inserir dados fictícios
clientes = [
    (1, 'Ana', 'São Paulo'),
    (2, 'Bruno', 'Rio de Janeiro'),
    (3, 'Carla', 'Belo Horizonte')
]

produtos = [
    (1, 'Camiseta', 'Vestuário', 59.90),
    (2, 'Tênis', 'Calçados', 199.90),
    (3, 'Boné', 'Acessórios', 39.90)
]

vendas = [
    (1, 1, 1, '2025-07-01', 2),
    (2, 1, 2, '2025-07-03', 1),
    (3, 2, 2, '2025-07-02', 1),
    (4, 3, 3, '2025-07-05', 3),
    (5, 3, 1, '2025-07-06', 1),
    (6, 2, 1, '2025-07-06', 2)
]

cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?)', clientes)
cursor.executemany('INSERT INTO produtos VALUES (?, ?, ?, ?)', produtos)
cursor.executemany('INSERT INTO vendas VALUES (?, ?, ?, ?, ?)', vendas)

conn.commit()
conn.close()

"/mnt/data/vendas_loja.db"
