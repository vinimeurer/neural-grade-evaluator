import streamlit as st
from neuronio import NeuronioAvaliador

# Configuração da página
st.set_page_config(
    page_title="Neurônio Avaliador",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilos e título
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Neurônio Avaliador de Notas")
st.markdown("---")

# Descrição
st.markdown("""
Este aplicativo utiliza um **neurônio artificial** para calcular a nota bimestral
baseado em diferentes avaliações com pesos personalizáveis.
""")

st.markdown("---")

# Sidebar para configuração dos pesos
st.sidebar.header("⚙️ Configuração dos Pesos")
st.sidebar.markdown("Defina a importância de cada avaliação:")

peso_trabalho = st.sidebar.slider(
    "Peso do Trabalho",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.05,
    help="Importância do trabalho na nota final"
)

peso_resumo = st.sidebar.slider(
    "Peso do Resumo",
    min_value=0.0,
    max_value=1.0,
    value=0.1,
    step=0.05,
    help="Importância do resumo na nota final"
)

peso_prova = st.sidebar.slider(
    "Peso da Prova",
    min_value=0.0,
    max_value=1.0,
    value=0.6,
    step=0.05,
    help="Importância da prova na nota final"
)

bias = st.sidebar.slider(
    "Bias (ajuste fino)",
    min_value=-2.0,
    max_value=2.0,
    value=0.0,
    step=0.1,
    help="Ajuste adicional à avaliação"
)

# Normalizar e validar pesos
soma_pesos = peso_trabalho + peso_resumo + peso_prova
st.sidebar.markdown("---")
st.sidebar.metric("Soma dos Pesos", f"{soma_pesos:.2f}")

# Conteúdo principal
st.header("📊 Inserir Notas")

col1, col2, col3 = st.columns(3)

with col1:
    nota_trabalho = st.number_input(
        "Nota do Trabalho (0-10)",
        min_value=0.0,
        max_value=10.0,
        value=9.9,
        step=0.1
    )

with col2:
    nota_resumo = st.number_input(
        "Nota do Resumo (0-10)",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1
    )

with col3:
    nota_prova = st.number_input(
        "Nota da Prova (0-10)",
        min_value=0.0,
        max_value=10.0,
        value=7.6,
        step=0.1
    )

st.markdown("---")

# Criar neurônio e calcular nota
neuronio = NeuronioAvaliador(
    peso_trabalho=peso_trabalho,
    peso_resumo=peso_resumo,
    peso_prova=peso_prova,
    bias=bias
)

nota_final = neuronio.calcular_nota(
    nota_trabalho=nota_trabalho,
    nota_resumo=nota_resumo,
    nota_prova=nota_prova
)

# Exibir resultado
st.header("✨ Resultado")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Nota Bimestral Final",
        value=f"{nota_final:.2f}",
        delta=f"de 10.0",
        delta_color="off"
    )

with col2:
    # Indicador de desempenho
    if nota_final >= 9.0:
        status = "🌟 Excelente"
        cor = "green"
    elif nota_final >= 7.0:
        status = "💪 Muito Bom"
        cor = "blue"
    elif nota_final >= 5.0:
        status = "👍 Bom"
        cor = "orange"
    else:
        status = "⚠️ Insuficiente"
        cor = "red"
    
    st.markdown(f"<h3 style='text-align: center; color: {cor};'>{status}</h3>", unsafe_allow_html=True)

# Exibir decomposição da nota
st.markdown("---")
st.header("📈 Decomposição da Nota")

col1, col2, col3 = st.columns(3)

with col1:
    contribuicao_trabalho = peso_trabalho * nota_trabalho
    st.metric("Contribuição Trabalho", f"{contribuicao_trabalho:.2f}")

with col2:
    contribuicao_resumo = peso_resumo * nota_resumo
    st.metric("Contribuição Resumo", f"{contribuicao_resumo:.2f}")

with col3:
    contribuicao_prova = peso_prova * nota_prova
    st.metric("Contribuição Prova", f"{contribuicao_prova:.2f}")

# Calcular soma ponderada
soma_ponderada = (
    peso_trabalho * nota_trabalho +
    peso_resumo * nota_resumo +
    peso_prova * nota_prova +
    bias
)

st.markdown("---")
st.subheader("🧮 Cálculo da Soma Ponderada")
st.latex(
    r"S = "
    f"{peso_trabalho:.2f} \\cdot {nota_trabalho:.1f} + "
    f"{peso_resumo:.2f} \\cdot {nota_resumo:.1f} + "
    f"{peso_prova:.2f} \\cdot {nota_prova:.1f} + "
    f"{bias:.2f}"
)
st.markdown(f"**Soma = `{soma_ponderada:.2f}`**")

# Visualização em barras
st.markdown("---")
st.subheader("📊 Distribuição de Contribuição")

dados_contribuicoes = {
    "Trabalho": round(contribuicao_trabalho, 2),
    "Resumo": round(contribuicao_resumo, 2),
    "Prova": round(contribuicao_prova, 2),
}

st.bar_chart(dados_contribuicoes)

# ----------------------------
# Saída
# ----------------------------
st.markdown("---")
st.header("📤 Saída (Axônio)")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Nota Bimestral Final",
        value=f"{nota_final:.2f}"
    )

with col2:
    if nota_final >= 6.0:
        st.success("✅ Aluno Aprovado")
    else:
        st.error("❌ Aluno Reprovado")

# Informações adicionais
st.markdown("---")
with st.expander("ℹ️ Como funciona o Neurônio Avaliador?"):
    st.markdown("""
    O neurônio artificial calcula a nota bimestral usando a seguinte fórmula:
    
    **Nota Final = (peso_trabalho × nota_trabalho) + (peso_resumo × nota_resumo) + (peso_prova × nota_prova) + bias**
    
    A nota final é limitada entre 0 e 10.
    
    - **Pesos**: Representam a importância relativa de cada avaliação
    - **Bias**: Um ajuste fino adicional que pode aumentar ou diminuir a nota
    - **Função de Ativação**: Garante que o resultado sempre fica entre 0 e 10
    """)

st.markdown("---")
st.caption("Desenvolvido com 🧠 Inteligência Artificial e Streamlit")
