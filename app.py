import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Design e Layout ---
st.set_page_config(
    page_title="Passos Mágicos: Previsão de Risco de Defasagem",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Imagem do logo da Associação
st.image("https://passosmagicos.org.br/wp-content/uploads/2020/10/Passos-magicos-icon-cor.png", width=150)

# Custom CSS para um design mais limpo e colorido (detalhes em azul, roxo, amarelo-ouro)
st.markdown(
    """
    <style>
    /* Cores da Paleta "Passos Mágicos" */
    :root {
        --magic-blue: #0A2342;
        --magic-purple: #5D3A8F;
        --magic-gold: #FFC400;
        --light-bg: #F5F5F5;
        --text-dark: #333333;
    }

    /* Geral */
    .stApp {
        background-color: var(--light-bg);
        color: var(--text-dark);
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: var(--magic-blue);
        font-weight: bold;
    }
    h1 {
        font-size: 2.5em;
        text-align: center;
        margin-top: 1em;
        margin-bottom: 0.5em;
    }
    h3 {
        font-size: 1.5em;
        color: var(--magic-purple);
        margin-top: 1em;
        margin-bottom: 0.8em;
    }

    /* Separadores */
    hr {
        border-top: 2px solid #ced4da;
        margin-top: 1.5em;
        margin-bottom: 1.5em;
    }

    /* Botões */
    .stButton>button {
        background-color: var(--magic-gold);
        color: var(--text-dark);
        border-radius: 8px;
        border: none;
        padding: 12px 25px;
        font-size: 1.2em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #e6b000; /* Tom mais escuro no hover */
        color: #ffffff;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    /* Sliders */
    .stSlider > div > div > div[data-testid="stSliderHandle"] {
        background-color: var(--magic-blue);
        border: 1px solid var(--magic-blue);
    }
    .stSlider > div > div > div[data-testid="stTrack"] {
        background-color: var(--magic-purple);
    }
    .stSlider > label {
        color: var(--magic-blue);
        font-weight: bold;
    }
    .stSelectbox > label, .stRadio > label, .stTextInput > label, .stDateInput > label {
        color: var(--magic-blue);
        font-weight: bold;
    }

    /* --- CORREÇÃO DAS MENSAGENS DE ALERTA --- */
    div[data-testid="stAlert"] {
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
    }
    /* Força todo o texto interno das Caixas de Alerta (sucesso/erro/info) a ser escuro */
    div[data-testid="stAlert"] * {
        color: #111111 !important;
        font-size: 1.05em !important;
    }
    
    /* Cor de fundo para Sucesso (Verde claro com texto bem escuro) */
    div[data-testid="stAlert"]:has(div[data-testid="stAlertContentSuccess"]) {
        background-color: #d4edda !important;
        border-left: 5px solid #28a745 !important;
    }
    
    /* Cor de fundo para Erro (Vermelho claro com texto bem escuro) */
    div[data-testid="stAlert"]:has(div[data-testid="stAlertContentError"]) {
        background-color: #f8d7da !important;
        border-left: 5px solid #dc3545 !important;
    }

    /* Texto informativo */
    .stMarkdown p {
        font-size: 1.05em;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✨ Passos Mágicos: Previsão de Risco de Defasagem Educacional")
st.markdown("--- ") # Separador visual

# Carregar o modelo treinado
model = joblib.load('modelo_passos_magicos.pkl')

st.write("### Insira os dados do aluno para prever o risco de aumento de defasagem no ano seguinte")

# Criar colunas para melhor layout de entrada de dados
col1, col2, col3 = st.columns(3)

with col1:
    ian = st.select_slider('IAN (Indicador de Adequação de Nível):', options=[2.5, 5.0, 10.0], value=5.0)
    ieg = st.slider('IEG (Engajamento):', 2.0, 10.0, 5.0, 0.1)

with col2:
    ips = st.slider('IPS (Aspectos Psicossociais):', 2.5, 10.0, 5.0, 0.1)
    ida = st.slider('IDA (Desempenho Acadêmico):', 0.0, 10.0, 5.0, 0.1)

with col3:
    iaa = st.slider('IAA (Autoavaliação):', 0.0, 10.0, 5.0, 0.1)
    tempo_de_casa_option = st.select_slider('Tempo de casa (em anos):', options=['0 anos', '1 ano', '2 anos', '3 ou mais anos'], value='1 ano')
    if tempo_de_casa_option == '0 anos':
        tempo_de_casa = 0
    elif tempo_de_casa_option == '1 ano':
        tempo_de_casa = 1
    elif tempo_de_casa_option == '2 anos':
        tempo_de_casa = 2
    else:
        tempo_de_casa = 3

# Calcular Discrepancia_Percepcao_Calculada
discrepancia_percepcao_calculada = ida - iaa

# Botão para fazer a previsão
if st.button('Prever Risco de Defasagem'):
    input_data = pd.DataFrame([[ian, ieg, ips, discrepancia_percepcao_calculada, tempo_de_casa]],
                              columns=['IAN', 'IEG', 'IPS', 'Discrepancia_Percepcao_Calculada', 'Tempo_de_casa_Calculado'])

    prediction = model.predict(input_data)[0]

    prediction_proba = model.predict_proba(input_data)[0]
    prob_sem_risco = prediction_proba[0] * 100
    prob_em_risco = prediction_proba[1] * 100

    st.markdown("--- ")
    st.write("### Resultado da Previsão:")

    if prediction == 1:
        st.error(
            f"**Atenção Recomendada**: Este aluno faz parte de um grupo de risco e precisa de uma atenção mais próxima.\n\n"
            f"*(O modelo identificou {prob_em_risco:.1f}% de chance de aumento de defasagem)*"
        )
    else:
        st.success(
            f"**Bom Sinal**: Este aluno apresenta um bom ritmo de desenvolvimento e baixo risco de defasagem.\n\n"
            f"*(Probabilidade estimada de estabilidade: {prob_sem_risco:.1f}%)*"
        )






    st.markdown("--- ")
    st.write("#### Sobre o Modelo:")
    st.markdown(
        """
        Este modelo de Machine Learning, baseado em **Random Forest**, foi treinado para prever a probabilidade de um aluno aumentar a defasagem educacional no ano seguinte.
        
        **Métricas Chave:**
        - **IAN (Indicador de Adequação de Nível):** Mede o nível de adequação do aluno ao currículo.
        - **IEG (Engajamento):** Reflete o nível de participação e interesse do aluno nas atividades.
        - **IPS (Aspectos Psicossociais):** Avalia fatores como autoestima, resiliência e relações sociais.
        - **IDA (Desempenho Acadêmico):** Representa a nota real do aluno em avaliações.
        - **IAA (Autoavaliação):** A percepção do próprio aluno sobre seu desempenho.
        - **Discrepância de Percepção (IDA - IAA):** A diferença entre o desempenho real e a autoavaliação, indicando um possível "viés de otimismo" ou subestimação.
        - **Tempo de Casa:** Número de anos que o aluno está no programa.

        O modelo busca identificar padrões nessas variáveis para indicar o risco de aumento de defasagem, auxiliando na tomada de decisões pedagógicas e sociais.
        """
    )

    st.markdown("--- ")
    st.write("#### Detalhes dos Dados de Entrada:")
    st.write(f"- IAN: {ian}")
    st.write(f"- IEG: {ieg}")
    st.write(f"- IPS: {ips}")
    st.write(f"- IDA: {ida}")
    st.write(f"- IAA: {iaa}")
    st.write(f"- Discrepância de Percepção (IDA - IAA): {discrepancia_percepcao_calculada:.2f}")
    st.write(f"- Tempo de Casa (Anos, limitado a 3): {tempo_de_casa}")

    st.markdown("--- ")
    st.markdown("***Nota:*** *Este modelo é uma ferramenta de apoio. A decisão final e as intervenções devem ser baseadas em uma análise pedagógica e social aprofundada.*")
