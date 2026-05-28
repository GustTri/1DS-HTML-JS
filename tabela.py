import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = [
    ["Picanha", 42.00, 68.90],
    ["Alcatra", 35.50, 57.90],
    ["Contra-filé", 38.00, 61.90],
    ["Costela Suína", 22.00, 39.90],
    ["Pernil", 19.50, 34.90],
    ["Peito de Frango", 14.00, 24.90],
    ["Coxa e Sobrecoxa", 11.50, 21.90],
    ["Costelinha", 20.50, 25.50],
    ["Acém", 24.00, 42.90],
    ["Toscana Artesanal", 17.00, 31.90],
    ["Bacon", 40.00, 45.00],
    ["Lagarto", 29.00, 48.90],
    ["Costela Bovina", 23.50, 41.90],
    ["Pé Suíno", 11.00, 19.90],
    ["Coração de Frango", 13.50, 24.50],
    ["Toscana Picante", 18.50, 34.90],
    ["Músculo", 22.00, 39.90],
    ["Costela Defumada", 27.00, 46.90],
    ["Filé de Frango", 16.00, 28.90],
    ["Linguiça de Frango", 10.50, 21.90],
    ["Filé Mignon", 58.00, 89.90],
    ["Joelho Suíno", 15.00, 27.90],
    ["Sobrecoxa Desossada", 14.50, 25.90],
    ["Salame Italiano", 35.00, 59.90],
    ["Rabada", 20.00, 36.90],
    ["Frango Caipira", 18.00, 32.90],
    ["Maminha", 36.00, 59.90],
    ["Fraldinha", 33.50, 55.90],
    ["Lombo Suíno", 21.00, 37.90],
    ["Asa de Frango", 10.00, 18.90],
    ["Filezinho Sassami", 15.50, 27.90],
    ["Sambiquira", 16.00, 29.90],
    ["Cupim", 28.00, 49.90],
    ["Paleta Suína", 18.50, 32.90],
    ["Frango Inteiro", 9.50, 16.90],
    ["Calabresa", 12.00, 19.90],
    ["Patinho", 31.00, 53.90],
    ["Torresmo", 25.00, 44.90],
    ["Moela", 8.50, 14.90],
]


df = pd.DataFrame(dados, columns=["Produto", "Compra", "Venda"])


sns.set(style="whitegrid")


plt.figure(figsize=(20, 8))

plt.plot(df["Produto"], df["Compra"],
         marker='o',
         linewidth=2,
         label='Preço de Compra',
         color='blue')
plt.plot(df["Produto"], df["Venda"],
         marker='o',
         linewidth=2,
         label='Preço de Venda',
         color='red')

plt.xticks(rotation=70)
plt.ylabel("Preço (R$)")
plt.xlabel("Produtos")
plt.title("Comparação entre Preço de Compra e Venda")
plt.legend()


plt.tight_layout()

plt.show()