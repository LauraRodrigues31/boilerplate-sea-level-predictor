import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Ler dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')

    # Criar gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Criar a primeira linha de melhor ajuste usando todos os dados
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))  # Anos de 1880 a 2050
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, color='red', label='Best Fit Line (1880-2050)')

    # Criar a segunda linha de melhor ajuste usando dados a partir do ano 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))  # Anos de 2000 a 2050
    y_pred_recent = intercept_recent + slope_recent * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (2000-2050)')

    # Adicionar rótulos e títuloo
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salvar o gráfico e retornar o eixo para testes
    plt.savefig('sea_level_plot.png')
    return plt.gca()
