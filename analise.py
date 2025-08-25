import pandas as pd
import matplotlib.pyplot as plt

# Define os nomes das colunas (mesma ordem do app.py)
colunas = ["timestamp", "nome", "idade", "cidade", "genero", "sono", "atividade", "bebida", "app"]

# Lê o CSV já com cabeçalho definido
df = pd.read_csv("respostas.csv", names=colunas, header=None)

# Remove a linha de cabeçalho duplicada se existir
df = df[df["nome"] != "nome"]

# Mostra as primeiras linhas
print("\n--- Primeiras respostas ---")
print(df.head())

# Estatísticas descritivas
print("\n--- Estatísticas ---")
print(df.describe(include="all"))

# Contagem de bebidas
print("\n--- Bebidas mais consumidas ---")
print(df["bebida"].value_counts())

# Média de idades
print("\n--- Média de idade ---")
print(df["idade"].astype(float).mean())

# -------------------------------
#  GRAFICOS
# -------------------------------

# Bebida mais consumida
df["bebida"].value_counts().plot(kind="bar", title="Bebida mais consumida")
plt.show()

# Aplicativo mais usado
df["app"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="App mais usado")
plt.ylabel("")  # tira o texto "app" do lado
plt.show()

# Sono por faixa
df["sono"].value_counts().plot(kind="barh", title="Horas de sono por noite")
plt.show()
