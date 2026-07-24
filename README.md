# 🎓 Datathon Passos Mágicos: Inteligência Artificial contra a Defasagem Escolar

Este repositório contém a solução completa desenvolvida para o **Datathon da Fase 5 (FIAP)**, focada nos dados da **Associação Passos Mágicos**. O objetivo é mensurar o impacto educacional da ONG e prever, via Machine Learning, quais alunos correm risco de aumentar sua defasagem escolar no ano seguinte.

## 🚀 Estrutura do Projeto

O projeto foi dividido em três frentes principais:
1.  **ETL:** Tratamento e limpeza de dados. *(Datathon_Passos_Mágicos_ETL.ipynb)*
2.  **EDA:** Análise Exploratória. *(Datathon_Passos_Mágicos_EDA.ipynb)*
3.  **Machine Learning:** Modelo preditivo focado em **Recall**, garantindo que nenhum aluno em risco seja ignorado pela instituição. *(Datathon_Passos_Mágicos_ML.ipynb)*
4.  **Deploy (Streamlit):** Aplicativo interativo para diagnóstico precoce por parte dos educadores.

## 💡 Principais Insights
*   **Eficiência Comprovada:** A elite educacional (Pedra Topázio) dobrou de tamanho entre 2022 e 2024.
*   **O Efeito Refúgio:** Alunos em risco costumam apresentar alto bem-estar emocional, o que pode mascarar dificuldades cognitivas silenciosas.
*   **Preditores de Risco:** O modelo de IA validou que o **IAN** (idade-série) e a **Discrepância de Percepção** são os maiores sinais de alerta.

## 🛠️ Tecnologias Utilizadas
*   Python (Pandas, Scikit-Learn)
*   Streamlit (Interface Web)
*   Matplotlib/Seaborn (Visualização de Dados)

## 💻 Como rodar o App
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o Streamlit: `streamlit run app.py`
