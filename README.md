# Análise e Predição de Renda

Este projeto visa analisar e prever a renda dos clientes com base em um conjunto de variáveis socioeconômicas. Utilizamos técnicas de análise exploratória de dados (AED), pré-processamento e modelagem preditiva para entender melhor as características dos dados e construir modelos de regressão capazes de estimar a renda.

## Tecnologias Utilizadas
- Python
- Pandas para manipulação de dados
- NumPy para operações numéricas
- Matplotlib e Seaborn para visualização de dados
- Scikit-learn para pré-processamento e modelagem
- ydata_profiling para análise exploratória de dados

## Processo de Análise

Iniciamos com uma análise exploratória detalhada para compreender a distribuição das variáveis, possíveis correlações e a necessidade de tratamento de dados, incluindo a manipulação de valores ausentes e outliers.

### Decisões Preliminares
- **Análise Exploratória dos Dados (AED)**: Primeira etapa para mapear a qualidade dos dados.
- **Tratamento de Dados**: Aplicação de técnicas para lidar com valores ausentes e outliers.
- **Seleção de Modelos**: Exploração inicial de modelos de Regressão Linear, Regressão de Ridge e K-Nearest Neighbors (KNN).
- **Avaliação de Modelos**: Utilização de métricas como MSE (Erro Quadrático Médio) e R² para avaliar os modelos.

### Pré-processamento de Dados
O pré-processamento incluiu a remoção de variáveis irrelevantes e duplicadas, tratamento de valores ausentes, e aplicação de One-Hot Encoding para variáveis categóricas. Também realizamos um tratamento de outliers para garantir que o modelo fosse treinado com dados mais representativos.

### Modelagem
Foram testados três modelos de regressão:
- **Regressão Linear**: A regressão linear mostrou um coeficiente R² de 0.1763, indicando uma capacidade limitada de explicar a variância da renda.
- **Regressão de Ridge**: Com um R² de 0.1799, a regressão de Ridge teve um desempenho ligeiramente melhor, sugerindo algum benefício da regularização.
- **K-Nearest Neighbors (KNN)**: O modelo KNN, com k=13, teve o desempenho mais fraco, com um R² de 0.1519.

### Conclusão
Os modelos testados apresentaram uma capacidade limitada de prever a renda, o que sugere a complexidade dos dados e a possibilidade de haver relações não capturadas pelos modelos. Este projeto destaca a importância do pré-processamento de dados e da seleção cuidadosa de modelos para trabalhar com variáveis socioeconômicas complexas.
