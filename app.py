import streamlit as st
import pandas as pd
import joblib

# Configuração da página
st.set_page_config(page_title="Passos Mágicos - Previsão de Risco", page_icon="🪄", layout="centered")

# Título da Aplicação
st.title("🪄 Portal do Educador: Previsão de Risco Futuro (XGBoost)")
st.markdown("""
Esta aplicação utiliza um modelo avançado de **Gradient Boosting (XGBoost)** para prever se um aluno da **Associação Passos Mágicos** corre o risco de **aumentar sua defasagem escolar no ano seguinte**, com base em seu contexto e indicadores atuais.
""")

# Carregando o Modelo Treinado
@st.cache_resource
def load_model():
    return joblib.load('modelo_risco_passos_magicos.pkl')

modelo = load_model()

# Criando o formulário para o usuário preencher na barra lateral (Sidebar)
st.sidebar.header("📊 Insira os Indicadores do Aluno:")

# Mantivemos a escala original (0 a 10) pois o XGBoost lida melhor com limites extremos
ida = st.sidebar.slider("Desempenho Acadêmico (IDA)", 1.0, 10.0, 6.7)
ieg = st.sidebar.slider("Engajamento (IEG)", 2.0, 10.0, 8.6)
ipv = st.sidebar.slider("Ponto de Virada (IPV)", 3.3, 10.0, 7.8)
iaa = st.sidebar.slider("Autoavaliação (IAA)", 0.0, 10.0, 7.7)
ips = st.sidebar.slider("Psicossocial (IPS)", 2.5, 10.0, 5.9)
ipp = st.sidebar.slider("Psicopedagógico (IPP)", 2.8, 10.0, 6.9)

# Variáveis de contexto
st.sidebar.markdown("---")
st.sidebar.subheader("Contexto do Aluno")
escola_publica_input = st.sidebar.radio("Estuda em Escola Pública?", ["Sim", "Não (Bolsista)"])
tempo_ong = st.sidebar.number_input("Tempo de ONG ('0' para calouros) ", min_value=0, max_value=7, value=1)

# Convertendo o contexto para número
escola_publica = 1 if escola_publica_input == "Sim" else 0

# Botão de Previsão
if st.sidebar.button("🔮 Calcular Risco para o Próximo Ano"):
    
    # Criando o DataFrame na ordem exata esperada pelo XGBoost
    dicionario_dados = {
        'IDA': [ida],
        'IEG': [ieg],
        'IPV': [ipv],
        'IAA': [iaa],
        'IPS': [ips],
        'IPP': [ipp],
        'Escola_Publica': [escola_publica],
        'Tempo_ONG': [tempo_ong]
    }
    dados_aluno = pd.DataFrame(dicionario_dados)
    
    # O XGBoost lida de forma nativa com a probabilidade calibrada
    previsao = modelo.predict(dados_aluno)[0] 
    probabilidade = modelo.predict_proba(dados_aluno)[0][1] * 100
    
    # Exibindo o resultado na tela principal
    st.subheader("Resultado da Análise Preditiva:")
    
    if int(previsao) == 1:
        st.error(f"⚠️ **ALERTA DE RISCO FUTURO!** Este aluno tem **{probabilidade:.1f}%** de probabilidade de **AUMENTAR sua defasagem escolar** no ano seguinte.")
        st.markdown("""
        **💡 Recomendação Pedagógica (Baseada na IA):**
        O modelo XGBoost identificou um padrão crítico de comportamento nos indicadores atuais. 
        Sugerimos uma intervenção proativa da equipe psicopedagógica para entender as quedas de rendimento e evitar a evasão ou o atraso escolar do aluno.
        """)
    else:
        st.success(f"✅ **BOM PROGNÓSTICO!** Este aluno apresenta apenas **{probabilidade:.1f}%** de risco de piorar sua defasagem no próximo ano.")
        st.markdown("""
        **💡 Recomendação:**
        O aluno demonstra estabilidade. Continue acompanhando os indicadores padrão para manter o desenvolvimento contínuo em sua jornada!
        """)