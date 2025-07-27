import streamlit as st

# Configuração básica
st.set_page_config(
    page_title="WebGIS - Wdias",
    page_icon="🗺️",
    layout="wide"
)

# Título
st.title("🗺️ WebGIS - Wdias Assessoria Rural")
st.markdown("---")

# Sistema de login simples
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("### 🔐 Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos!")
    st.stop()

# Conteúdo principal após login
st.success("✅ Logado como Admin")

# Mapa simples usando HTML
st.subheader("🗺️ Mapa Interativo")

# Criar mapa usando HTML/JavaScript
map_html = """
<div style="width: 100%; height: 500px; background: #f0f0f0; border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-direction: column;">
    <div style="font-size: 3rem; margin-bottom: 1rem;">🗺️</div>
    <div style="font-size: 1.5rem; color: #1f4e79; margin-bottom: 1rem;">Mapa Interativo</div>
    <div style="text-align: center; color: #666;">
        <p>📍 Propriedade 1 - 150 hectares</p>
        <p>📍 Propriedade 2 - 200 hectares</p>
        <p>📍 Propriedade 3 - 300 hectares</p>
    </div>
    <div style="margin-top: 2rem;">
        <button onclick="alert('Funcionalidade de mapa será implementada em breve!')" 
                style="background: #1f4e79; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
            🗺️ Ver Mapa Completo
        </button>
    </div>
</div>
"""

st.markdown(map_html, unsafe_allow_html=True)

# Informações das propriedades
st.subheader("📊 Propriedades")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Propriedade 1", "150 hectares", "Agricultura")
    st.info("📍 Localização: São Paulo, SP")

with col2:
    st.metric("Propriedade 2", "200 hectares", "Pecuária")
    st.info("📍 Localização: Minas Gerais, MG")

with col3:
    st.metric("Propriedade 3", "300 hectares", "Mista")
    st.info("📍 Localização: Goiás, GO")

# Sidebar
with st.sidebar:
    st.header("📊 Informações")
    st.write("**WebGIS - Wdias**")
    st.write("Sistema de Informações Geográficas")
    
    st.header("🔧 Opções")
    if st.button("🔄 Recarregar"):
        st.rerun()
    
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    st.header("📋 Estatísticas")
    st.metric("Total de Propriedades", "3")
    st.metric("Área Total", "650 hectares")
    st.metric("Estados", "3")

# Footer
st.markdown("---")
st.markdown("**Desenvolvido por Wdias Assessoria Rural**")
st.markdown("*Sistema de Informações Geográficas*")