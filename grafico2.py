import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Dados fornecidos
dados = {
    "Corte": [
        "Picanha", "Alcatra", "Contra-filé", "Costela Suína", "Pernil", 
        "Peito de Frango", "Coxa e Sobrecoxa", "Costelinha", "Acém", "Toscana Artesanal",
        "Bacon", "Lagarto", "Costela Bovina", "Pé Suíno", "Coração de Frango",
        "Toscana Picante", "Músculo", "Costela Defumada", "Filé de Frango", "linguiça de frango",
        "Filé Mignon", "Joelho Suíno", "Sobrecoxa Desossada", "Salame Italiano 1", "Rabada",
        "Frango Caipira", "Maminha", "Fraldinha", "Lombo Suíno", "Asa de Frango",
        "Filezinho Sassami", "Sambiquira", "Cupim", "Paleta Suína", "Frango Inteiro",
        "Suína", "Patinho", "Torresmo", "Moela", "Salame Italiano 2"
    ],
    "Peso (kg)": [
        12.5, 18.0, 20.0, 10.0, 25.0, 30.0, 22.0, 14.0, 16.0, 14.0,
        16.5, 18.0, 30.0, 12.0, 9.0, 15.0, 21.0, 17.0, 26.0, 11.0,
        10.0, 13.0, 20.0, 8.0, 19.0, 28.0, 15.0, 17.5, 20.0, 18.0,
        12.0, 10.0, 13.0, 19.0, 35.0, 20.0, 14.0, 8.0, 11.0, 13.0
    ],
    "Preço Custo (R$)": [
        42.0, 35.5, 38.0, 22.0, 19.5, 14.0, 11.5, 20.5, 24.0, 17.0,
        40.0, 29.0, 23.5, 11.0, 13.5, 18.5, 22.0, 27.0, 16.0, 10.5,
        58.0, 15.0, 14.5, 35.0, 20.0, 18.0, 36.0, 33.5, 21.0, 10.0,
        15.5, 16.0, 28.0, 18.5, 9.5, 12.0, 31.0, 25.0, 8.5, 18.0
    ],
    "Preço Venda (R$)": [
        68.9, 57.9, 61.9, 39.9, 34.9, 24.9, 21.9, 25.5, 42.9, 31.9,
        45.0, 48.9, 41.9, 19.9, 24.5, 34.9, 39.9, 46.9, 28.9, 21.9,
        89.9, 27.9, 25.9, 59.9, 36.9, 32.9, 59.9, 55.9, 37.9, 18.9,
        27.9, 29.9, 49.9, 32.9, 16.9, 19.9, 53.9, 44.9, 14.9, 33.9
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Criando uma coluna de lucro para selecionar os destaques (evita poluição visual de 40 itens juntos)
df['Lucro'] = df['Preço Venda (R$)'] - df['Preço Custo (R$)']
df_filtrado = df.nlargest(5, 'Lucro')  # Seleciona os 5 cortes mais lucrativos para o radar

# 2. Configuração do Gráfico de Radar
categorias = ['Peso (kg)', 'Preço Custo (R$)', 'Preço Venda (R$)']
num_vars = len(categorias)

# Calculando os ângulos para cada métrica no círculo
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angulos += angulos[:1]  # Fecha o círculo do radar

# Inicializando o gráfico polar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Cores para cada corte selecionado
cores = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33F3']

# 3. Plotando os dados de cada corte
for i, (idx, linha) in enumerate(df_filtrado.iterrows()):
    valores = [linha['Peso (kg)'], linha['Preço Custo (R$)'], linha['Preço Venda (R$)']]
    valores += valores[:1]  # Fecha o círculo do corte
    
    # Desenha a linha
    ax.plot(angulos, valores, color=cores[i], linewidth=2, label=linha['Corte'])
    # Preenche a área sob a linha
    ax.fill(angulos, valores, color=cores[i], alpha=0.1)

# Fixando as etiquetas dos eixos (as pontas da teia)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angulos[:-1], categorias, color='grey', size=12)

# Ajustando a escala visual do gráfico
ax.set_rlabel_position(0)
plt.yticks([20, 40, 60, 80], ["20", "40", "60", "80"], color="grey", size=10)
plt.ylim(0, 100)

# Título e Legenda
plt.title("Gráfico de Radar - Top 5 Cortes por Lucratividade", size=16, color='black', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

# Exibir o gráfico
plt.tight_layout()
plt.show()                    