import streamlit as st
import folium
from streamlit_folium import st_folium

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

# Criar mapa simples
st.subheader("🗺️ Mapa Interativo")

# Dados de exemplo
sample_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Propriedade 1",
                "area": "150 hectares"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-46.6388, -23.5489],
                    [-46.6388, -23.5480],
                    [-46.6370, -23.5480],
                    [-46.6370, -23.5489],
                    [-46.6388, -23.5489]
                ]]
            }
        }
    ]
}

# Criar mapa
try:
    m = folium.Map(
        location=[-23.5489, -46.6388],
        zoom_start=15,
        tiles='OpenStreetMap'
    )
    
    # Adicionar dados
    folium.GeoJson(
        sample_data,
        name="Propriedades",
        style_function=lambda x: {
            'fillColor': '#FF6B6B',
            'color': '#1f4e79',
            'weight': 2,
            'fillOpacity': 0.7
        },
        popup=folium.GeoJsonPopup(
            fields=['name', 'area'],
            aliases=['Nome:', 'Área:'],
            localize=True
        )
    ).add_to(m)
    
    # Exibir mapa
    st_folium(m, width=700, height=500)
    
except Exception as e:
    st.error(f"Erro ao carregar mapa: {str(e)}")
    st.info("Carregando mapa básico...")
    
    # Mapa de fallback
    m = folium.Map(location=[-23.5489, -46.6388], zoom_start=10)
    st_folium(m, width=700, height=500)

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

# Footer
st.markdown("---")
st.markdown("**Desenvolvido por Wdias Assessoria Rural**")