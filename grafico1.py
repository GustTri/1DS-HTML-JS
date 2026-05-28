import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Produto": [
        "Picanha", "Alcatra", "Contra-filé", "Costela Suína", "Pernil", 
        "Peito de Frango", "Coxa/Sobrecoxa", "Costelinha", "Acém", "Toscana Art.",
        "Bacon", "Lagarto", "Costela Bov.", "Pé Suíno", "Coração Frango", 
        "Toscana Pic.", "Músculo", "Costela Def.", "Filé de Frango", "Ling. Frango",
        "Filé Mignon", "Joelho Suíno", "Sobrecoxa Des.", "Salame Ital. 1", "Rabada", 
        "Frango Caip.", "Maminha", "Fraldinha", "Lombo Suíno", "Asa de Frango",
        "Filez. Sassami", "Sambiquira", "Cupim", "Paleta Suína", "Frango Int.", 
        "Suína", "Patinho", "Torresmo", "Moela", "Salame Ital. 2"
    ],
    "Volume": [12.5, 18.0, 20.0, 10.0, 25.0, 30.0, 22.0, 14.0, 16.0, 14.0, 
               16.5, 18.0, 30.0, 12.0, 9.0, 15.0, 21.0, 17.0, 26.0, 11.0, 
               10.0, 13.0, 20.0, 8.0, 19.0, 28.0, 15.0, 17.5, 20.0, 18.0, 
               12.0, 10.0, 13.0, 19.0, 35.0, 20.0, 14.0, 8.0, 11.0, 13.0],
    "Preço Custo": [42.0, 35.5, 38.0, 22.0, 19.5, 14.0, 11.5, 20.5, 24.0, 17.0, 
                     40.0, 29.0, 23.5, 11.0, 13.5, 18.5, 22.0, 27.0, 16.0, 10.5, 
                     58.0, 15.0, 14.5, 35.0, 20.0, 18.0, 36.0, 33.5, 21.0, 10.0, 
                     15.5, 16.0, 28.0, 18.5, 9.5, 12.0, 31.0, 25.0, 8.5, 18.0],
    "Preço Venda": [68.9, 57.9, 61.9, 39.9, 34.9, 24.9, 21.9, 25.5, 42.9, 31.9, 
                     45.0, 48.9, 41.9, 19.9, 24.5, 34.9, 39.9, 46.9, 28.9, 21.9, 
                     89.9, 27.9, 25.9, 59.9, 36.9, 32.9, 59.9, 55.9, 37.9, 18.9, 
                     27.9, 29.9, 49.9, 32.9, 16.9, 19.9, 53.9, 44.9, 14.9, 33.9]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(14, 7))

plt.stackplot(df["Produto"], df["Volume"], df["Preço Custo"], df["Preço Venda"], 
              labels=["Volume (kg/unid)", "Preço de Custo (R$)", "Preço de Venda (R$)"],
              colors=["#3498db", "#e67e22", "#2ecc71"], alpha=0.8)

plt.title("Análise de Produtos: Volume vs Custo vs Venda", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Produtos", fontsize=12, labelpad=10)
plt.ylabel("Valores / Escala", fontsize=12, labelpad=10)
plt.xticks(rotation=45, ha="right", fontsize=9)
plt.legend(loc="upper right", fontsize=11)
plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
