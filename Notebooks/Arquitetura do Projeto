## 📂 Entendendo os Notebooks

A jornada de dados deste projeto foi construída de forma sequencial, dividida em três Notebooks principais e uma aplicação web. A leitura e execução devem seguir esta ordem lógica:

### 1. `Datathon_Passos_Mágicos_ETL.ipynb` (Preparação de Dados)
*   **O que faz:** É a fundação do projeto. Ele consolida as bases da PEDE de 2022, 2023 e 2024 em um único repositório.
*   **Destaque:** Além de limpar, padronizar e tratar nulos, este arquivo cria a inteligência temporal do projeto ao construir a variável alvo `Aumento_Df_Ano_Seguinte`. É aqui que rastreamos os alunos que efetivamente pioraram a defasagem escolar no ano seguinte para ensinar o algoritmo de IA.

### 2. `Datathon_Passos_Mágicos_EDA.ipynb` (Análise Exploratória)
*   **O que faz:** Focado em *Storytelling* Gerencial, responde às 11 dores de negócio propostas pela ONG através de visualização de dados e estatística (como correlação de Pearson). 
*   **Destaque:** Descobre padrões de risco invisíveis à intuição humana, como o **Paradoxo da Fase 0** (46,9% das reprovações estão na alfabetização), o **Efeito Refúgio** (apoio psicossocial camuflando o declínio acadêmico), e o **Viés de Otimismo** (a desconexão perigosa entre a nota real e a autoavaliação do aluno).

### 3. `Datathon_Passos_Mágicos_ML.ipynb` (Modelo Preditivo)
*   **O que faz:** Recebe a base final e as descobertas do EDA para treinar Inteligências Artificiais (Random Forest e XGBoost) a fim de prever o risco de retenção/piora escolar do aluno.
*   **Destaque:** O desenvolvimento técnico foi ancorado no negócio: otimizamos a métrica de **Recall** (capturando mais de 69% dos alunos em risco real no teste), assegurando que a ONG "não deixe ninguém para trás". A extração de *Feature Importance* validou estatisticamente as teses criadas no EDA (com o IAN e a Discrepância de percepção liderando a importância).
