import streamlit as st
from streamlit_folium import st_folium
import folium
import json
import os
import numpy as np
import glob

# Tentar importar geopandas, mas não falhar se não conseguir
try:
    import geopandas as gpd
    GEOPANDAS_AVAILABLE = True
except ImportError:
    GEOPANDAS_AVAILABLE = False
    st.warning("⚠️ GeoPandas não está disponível. Usando dados de exemplo.")

# Procurar automaticamente o primeiro arquivo .shp na pasta atual
def encontrar_shapefile():
    arquivos = glob.glob("*.shp")
    if arquivos:
        return arquivos[0]
    else:
        return None

shapefile_path = encontrar_shapefile()

# Lista de usuários e senhas
usuarios = {
    "admin": "senhaadm",
    "usuario1": "senha1",
    "usuario2": "senha2",
    "deluccasgma@gmail.com": "Lg1401@@",
    "gilmar@wdias.eng.br": "123456"
}

# Lista de administradores
admins = ["admin", "deluccasgma@gmail.com"]

# Configuração da página
st.set_page_config(
    page_title="WebGIS - Wdias Assessoria Rural e Engenharia",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tela de login
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80');
            background-size: cover;
            background-position: center;
        }
        .login-box {
            background: rgba(255,255,255,0.95);
            padding: 2rem 2rem 1.5rem 2rem;
            border-radius: 16px;
            max-width: 400px;
            margin: 100px auto 0 auto;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
        }
        .login-title {
            text-align: center;
            color: #1f4e79;
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .login-subtitle {
            text-align: center;
            color: #2e7d32;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🗺️ WebGIS</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Wdias Assessoria Rural e Engenharia</div>', unsafe_allow_html=True)
    usuario = st.text_input("👤 Usuário")
    senha = st.text_input("🔒 Senha", type="password")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Entrar", use_container_width=True):
            if usuario in usuarios and usuarios[usuario] == senha:
                st.session_state.autenticado = True
                st.session_state.usuario = usuario
                st.success(f"Bem-vindo, {usuario}! 🎉")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# Mensagem especial para administradores
if st.session_state.get("usuario") in admins:
    st.sidebar.success("👑 Você está logado como ADMINISTRADOR.")

# Título principal
st.title("🗺️ WebGIS - Sistema de Informações Geográficas")
st.markdown("---")

# Sidebar para configurações
st.sidebar.title("⚙️ Configurações do Mapa")

# Carregar dados geoespaciais
geojson_data = None
center = [-23.5489, -46.6388]  # São Paulo como padrão

if GEOPANDAS_AVAILABLE and shapefile_path:
    try:
        gdf = gpd.read_file(shapefile_path)
        geojson_data = gdf.__geo_interface__
        
        # Exibir informações do shapefile
        st.sidebar.success(f"✅ Shapefile carregado: {os.path.basename(shapefile_path)}")
        st.sidebar.info(f"📊 Número de feições: {len(gdf)}")
        
        # Mostrar atributos disponíveis
        if not gdf.empty:
            st.sidebar.subheader("📋 Atributos disponíveis:")
            for col in gdf.columns:
                if col != 'geometry':
                    st.sidebar.text(f"• {col}")
        
        # Calcular centroide para centralizar o mapa
        if geojson_data["features"]:
            geometry = geojson_data["features"][0]["geometry"]
            coords = geometry["coordinates"]
            if geometry["type"] == "Polygon":
                # Calcular centroide simples
                x_coords = [p[0] for p in coords[0]]
                y_coords = [p[1] for p in coords[0]]
                center = [sum(y_coords)/len(y_coords), sum(x_coords)/len(x_coords)]
            elif geometry["type"] == "MultiPolygon":
                # Pega o primeiro polígono do multipolígono
                x_coords = [p[0] for p in coords[0][0]]
                y_coords = [p[1] for p in coords[0][0]]
                center = [sum(y_coords)/len(y_coords), sum(x_coords)/len(x_coords)]
        
    except Exception as e:
        st.sidebar.error(f"❌ Erro ao carregar shapefile: {e}")
        geojson_data = None

# Se não conseguiu carregar shapefile, usar dados de exemplo
if geojson_data is None:
    st.sidebar.warning("⚠️ Usando dados de exemplo")
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "nome": "Área do Imóvel",
                    "area_ha": "150.5",
                    "proprietario": "João Silva",
                    "municipio": "São Paulo"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [-46.6388, -23.5489],
                        [-46.6388, -23.5480],
                        [-46.6378, -23.5480],
                        [-46.6378, -23.5489],
                        [-46.6388, -23.5489]
                    ]]
                }
            }
        ]
    }

# Opções do mapa
show_shapefile = st.sidebar.checkbox("🗺️ Exibir Shapefile", value=True)
show_popup = st.sidebar.checkbox("💬 Exibir Popups", value=True)
show_measure = st.sidebar.checkbox("📏 Ferramenta de Medição", value=True)

# Criar o mapa folium
m = folium.Map(
    location=center, 
    zoom_start=16, 
    control_scale=True,
    tiles=None
)

# Adicionar mapas de fundo
folium.TileLayer(
    "OpenStreetMap", 
    name="🗺️ OpenStreetMap",
    overlay=False,
    control=True
).add_to(m)

folium.TileLayer(
    "Stamen Terrain",
    name="🏔️ Stamen Terrain",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors",
    overlay=False,
    control=True
).add_to(m)

folium.TileLayer(
    "CartoDB positron",
    name="📰 CartoDB Positron",
    attr="©OpenStreetMap, ©CartoDB",
    overlay=False,
    control=True
).add_to(m)

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    name="🛰️ Satélite (Esri)",
    attr="Tiles © Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
    overlay=False,
    control=True
).add_to(m)

# Adicionar GeoJSON como camada
if show_shapefile:
    # Configurar popup baseado nos atributos disponíveis
    popup_fields = []
    if show_popup and geojson_data["features"]:
        popup_fields = list(geojson_data["features"][0]["properties"].keys())
    
    folium.GeoJson(
        geojson_data,
        name="🏠 Área do Imóvel",
        popup=folium.GeoJsonPopup(fields=popup_fields) if popup_fields else None,
        style_function=lambda feature: {
            'fillColor': '#ff7800',
            'color': '#000000',
            'weight': 2,
            'fillOpacity': 0.3
        },
        tooltip=folium.GeoJsonTooltip(fields=popup_fields) if popup_fields else None
    ).add_to(m)

# Adicionar ferramenta de medição se habilitada
if show_measure:
    folium.plugins.MeasureControl(
        position='topleft',
        primary_length_unit='meters',
        secondary_length_unit='kilometers',
        primary_area_unit='sqmeters',
        secondary_area_unit='acres'
    ).add_to(m)

# Adicionar controles extras
folium.plugins.Fullscreen(
    position='topright',
    title='Expandir mapa',
    title_cancel='Sair da tela cheia',
    force_separate_button=True
).add_to(m)

folium.plugins.MousePosition().add_to(m)

# Adicionar controle de camadas
folium.LayerControl(position='topright').add_to(m)

# Informações do usuário
st.sidebar.markdown("---")
st.sidebar.markdown(f"👤 **Usuário:** {st.session_state.get('usuario', 'N/A')}")
if st.sidebar.button("🚪 Logout"):
    st.session_state.autenticado = False
    st.rerun()

# Exibir o mapa
st.markdown("<style>div.block-container{padding-top:0rem;padding-bottom:0rem;}</style>", unsafe_allow_html=True)
st.markdown("### 🗺️ Visualização do Mapa")
st_folium(m, width=None, height=700)

# Informações adicionais
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("🗺️ **WebGIS** - Sistema de Informações Geográficas")
with col2:
    st.info("🏢 **Wdias** - Assessoria Rural e Engenharia")
with col3:
    st.info("📧 **Contato:** gilmar@wdias.eng.br") 