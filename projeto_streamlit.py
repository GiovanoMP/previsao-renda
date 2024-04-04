import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configurações do Seaborn para os gráficos
sns.set(context='talk', style='whitegrid')

# Configurações da página Streamlit
st.set_page_config(
     page_title="Análise de Previsão de Renda",
     page_icon="💰",
     layout="wide",
)

st.title('Análise exploratória e modelagem para previsão de renda')

# Introdução sobre o trabalho
st.markdown("""
## Entendimento do Negócio
Em um ambiente econômico cada vez mais dinâmico, a capacidade de prever a renda individual torna-se crucial para uma variedade de aplicações práticas, desde a avaliação de crédito até o planejamento financeiro pessoal. [...]
""")

# Discussão sobre os dados disponíveis
st.markdown("""
## Discussão Sobre os Dados Disponíveis
Foi apresentado e discutido o conjunto de dados a ser utilizado no projeto, que inclui variáveis demográficas e socioeconômicas importantes para a previsão de renda. [...]
""")

# Carregando e preparando os dados
renda = pd.read_csv('previsao_de_renda.csv')
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

# Análise exploratória dos dados
st.header('Análise Exploratória dos Dados')

# Distribuição da renda
st.subheader('Distribuição da Renda')
fig, ax = plt.subplots()
sns.histplot(renda['renda'], bins=30, ax=ax)
ax.set_title('Distribuição da Renda')
st.pyplot(fig)

# Distribuição do tempo de emprego
st.subheader('Distribuição do Tempo de Emprego')
tempo_emprego = renda['tempo_emprego']
fig, ax = plt.subplots(figsize=(10, 6))
plt.hist(tempo_emprego, bins=30, alpha=0.7, color='blue')
plt.title('Distribuição do Tempo de Emprego')
plt.xlabel('Tempo de Emprego (anos)')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75)
st.pyplot(fig)

# Boxplots
st.subheader('Análise de Outliers')
fig, axs = plt.subplots(2, 3, figsize=(20, 10))
sns.boxplot(y=renda['qtd_filhos'], ax=axs[0, 0])
axs[0, 0].set_title('Distribuição de Qtd_filhos')

sns.boxplot(y=renda['idade'], ax=axs[0, 1])
axs[0, 1].set_title('Distribuição de Idade')

sns.boxplot(y=renda['tempo_emprego'], ax=axs[0, 2])
axs[0, 2].set_title('Distribuição de Tempo_emprego')

sns.boxplot(y=renda['qt_pessoas_residencia'], ax=axs[1, 0])
axs[1, 0].set_title('Distribuição de Qt_pessoas_residencia')

sns.boxplot(y=renda['renda'], ax=axs[1, 1])
axs[1, 1].set_title('Distribuição de Renda')

# Ajuste de layout dos gráficos
plt.tight_layout()
st.pyplot(fig)

# Resultados dos modelos
st.header('## Resultados dos Modelos de Regressão')

st.markdown("""
### Regressão Linear
- **MSE**: 11,165,618.62
- **R²**: 0.1763

### Regressão de Ridge
- **MSE**: 11,116,549.75
- **R²**: 0.1799

### K-Neighbors Regressor
- **MSE**: 11,495,876.32
- **R²**: 0.1519

**Discussão dos Resultados:**
Os valores de MSE altos e R² abaixo de 0.2 para todos os modelos indicam que a capacidade preditiva é limitada com os recursos e técnicas atuais. [...]
""")
