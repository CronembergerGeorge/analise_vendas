import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar ao banco
conn = sqlite3.connect("data/vendas_loja.db") 

# Funções de análise
def receita_produto():
    df = pd.read_sql_query("""
        SELECT p.nome AS produto, SUM(v.quantidade * p.preco) AS receita
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id_produto
        GROUP BY p.nome
    """, conn)
    return df.sort_values(by="receita", ascending=False)

def total_cliente():
    df = pd.read_sql_query("""
        SELECT c.nome AS cliente, SUM(v.quantidade * p.preco) AS total
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id_produto
        JOIN clientes c ON v.id_cliente = c.id_cliente
        GROUP BY c.nome
    """, conn)
    return df.sort_values(by="total", ascending=False)

def receita_cidade():
    df = pd.read_sql_query("""
        SELECT c.cidade, SUM(v.quantidade * p.preco) AS receita
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id_produto
        JOIN clientes c ON v.id_cliente = c.id_cliente
        GROUP BY c.cidade
    """, conn)
    return df.sort_values(by="receita", ascending=False)

# Obter os DataFrames
df1 = receita_produto()
df2 = total_cliente()
df3 = receita_cidade()

# Visualização agrupada
fig, axes = plt.subplots(1, 3, figsize=(18, 5))  # 1 linha, 3 gráficos

cores = ["#4C72B0", "#DD8452", "#55A868"]

df1.plot(kind="bar", x="produto", y="receita", ax=axes[0], color=cores[0], legend=False)
axes[0].set_title("Receita por Produto")
axes[0].set_ylabel("R$")

df2.plot(kind="bar", x="cliente", y="total", ax=axes[1], color=cores[1], legend=False)
axes[1].set_title("Total por Cliente")
axes[1].set_ylabel("R$")

df3.plot(kind="bar", x="cidade", y="receita", ax=axes[2], color=cores[2], legend=False)
axes[2].set_title("Receita por Cidade")
axes[2].set_ylabel("R$")

plt.tight_layout()
plt.savefig("analise_vendas.png", dpi=300)
plt.show()

# Exportar para Excel (opcional)
with pd.ExcelWriter("analise_vendas.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Receita_Produto", index=False)
    df2.to_excel(writer, sheet_name="Total_Cliente", index=False)
    df3.to_excel(writer, sheet_name="Receita_Cidade", index=False)

# Fechar conexão
conn.close()
