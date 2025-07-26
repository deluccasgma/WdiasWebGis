import streamlit as st
from streamlit_folium import st_folium
import folium
import json
import os
import numpy as np
import glob
import geopandas as gpd
from folium.plugins import MarkerCluster, HeatMap, Fullscreen, MiniMap
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="WebGIS - Wdias Assessoria Rural e Engenharia",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para encontrar shapefiles na raiz do projeto
def encontrar_shapefiles():
    arquivos = glob.glob("*.shp")
    return arquivos

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
            background: rgba(255,255,255,0.85);
            padding: 2rem 2rem 1.5rem 2rem;
            border-radius: 16px;
            max-width: 350px;
            margin: 100px auto 0 auto;
            box-shadow: 0 4px 32px rgba(0,0,0,0.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.title("🗺️ WebGIS")
    st.markdown('<div style="text-align:center;font-size:1.1rem;margin-bottom:1rem;color:#2e7d32;font-weight:bold;">Wdias Assessoria Rural e Engenharia</div>', unsafe_allow_html=True)
    usuario = st.text_input("👤 Usuário")
    senha = st.text_input("🔒 Senha", type="password")
    if st.button("🚀 Entrar", type="primary"):
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

# Header principal
st.title("🗺️ WebGIS - Wdias Assessoria Rural e Engenharia")
st.markdown("---")

# Encontrar shapefiles disponíveis
shapefiles = encontrar_shapefiles()

if not shapefiles:
    st.error("❌ Nenhum arquivo .shp encontrado no projeto. Por favor, adicione shapefiles para visualizar o mapa.")
    st.stop()

# Sidebar para configurações
st.sidebar.title("⚙️ Configurações do Mapa")

# Seleção de shapefile
shapefile_selecionado = st.sidebar.selectbox(
    "📁 Selecionar Shapefile:",
    shapefiles,
    index=0
)

# Opções de visualização
show_shapefile = st.sidebar.checkbox("🗺️ Exibir Shapefile", value=True)
show_popup = st.sidebar.checkbox("💬 Mostrar Popups", value=True)
show_centroid = st.sidebar.checkbox("📍 Mostrar Centroide", value=False)

# Estilo do shapefile
st.sidebar.subheader("🎨 Estilo do Shapefile")
fill_color = st.sidebar.color_picker("Cor de Preenchimento", "#3388ff")
fill_opacity = st.sidebar.slider("Opacidade de Preenchimento", 0.0, 1.0, 0.3)
border_color = st.sidebar.color_picker("Cor da Borda", "#000000")
border_width = st.sidebar.slider("Espessura da Borda", 1, 10, 2)

# Carregar o Shapefile selecionado
try:
    gdf = gpd.read_file(shapefile_selecionado)
    geojson_data = gdf.__geo_interface__
    
    # Exibir informações do shapefile
    st.sidebar.subheader("📊 Informações do Shapefile")
    st.sidebar.write(f"**Arquivo:** {shapefile_selecionado}")
    st.sidebar.write(f"**Geometrias:** {len(gdf)}")
    st.sidebar.write(f"**Sistema de Coordenadas:** {gdf.crs}")
    
    # Mostrar atributos disponíveis
    if not gdf.empty:
        st.sidebar.write("**Atributos disponíveis:**")
        for col in gdf.columns:
            if col != 'geometry':
                st.sidebar.write(f"• {col}")
    
except Exception as e:
    st.error(f"❌ Erro ao carregar o arquivo Shapefile: {e}")
    st.stop()

# Calcular centroide do polígono
def calcular_centroide(coords):
    if isinstance(coords[0], list) and len(coords[0]) > 0:
        if isinstance(coords[0][0], list):  # MultiPolygon
            coords = coords[0]
        x = [p[0] for p in coords[0]]
        y = [p[1] for p in coords[0]]
        area = 0.0
        cx = 0.0
        cy = 0.0
        n = len(coords[0]) - 1
        for i in range(n):
            fator = x[i] * y[i+1] - x[i+1] * y[i]
            area += fator
            cx += (x[i] + x[i+1]) * fator
            cy += (y[i] + y[i+1]) * fator
        area *= 0.5
        if area == 0:
            return [y[0], x[0]]
        cx /= (6.0 * area)
        cy /= (6.0 * area)
        return [cy, cx]
    return [0, 0]

# Calcular centroide para centralizar o mapa
if geojson_data["features"]:
    geometry = geojson_data["features"][0]["geometry"]
    coords = geometry["coordinates"]
    if geometry["type"] == "Polygon":
        center = calcular_centroide(coords)
    elif geometry["type"] == "MultiPolygon":
        center = calcular_centroide(coords[0])
    else:
        center = [0, 0]
else:
    center = [0, 0]

# Criar o mapa folium
m = folium.Map(
    location=center, 
    zoom_start=16, 
    control_scale=True,
    tiles=None
)

# Adicionar mapas de fundo
folium.TileLayer("OpenStreetMap", name="🗺️ OpenStreetMap", overlay=False).add_to(m)
folium.TileLayer(
    "Stamen Terrain",
    name="🏔️ Stamen Terrain",
    overlay=False,
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors"
).add_to(m)
folium.TileLayer(
    "CartoDB positron",
    name="⚪ CartoDB Positron",
    overlay=False,
    attr="©OpenStreetMap, ©CartoDB"
).add_to(m)
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    name="🛰️ Satélite (Esri)",
    overlay=False,
    attr="Tiles © Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
).add_to(m)

# Adicionar GeoJSON como camada
if show_shapefile:
    # Configurar popup baseado nos atributos disponíveis
    popup_fields = None
    if show_popup and not gdf.empty:
        popup_fields = [col for col in gdf.columns if col != 'geometry']
    
    folium.GeoJson(
        geojson_data,
        name="📁 Shapefile",
        popup=folium.GeoJsonPopup(fields=popup_fields) if popup_fields else None,
        style_function=lambda feature: {
            'fillColor': fill_color,
            'color': border_color,
            'weight': border_width,
            'fillOpacity': fill_opacity
        }
    ).add_to(m)
    
    # Adicionar centroide se solicitado
    if show_centroid and geojson_data["features"]:
        geometry = geojson_data["features"][0]["geometry"]
        coords = geometry["coordinates"]
        if geometry["type"] == "Polygon":
            centroid = calcular_centroide(coords)
        elif geometry["type"] == "MultiPolygon":
            centroid = calcular_centroide(coords[0])
        else:
            centroid = center
            
        folium.Marker(
            location=centroid,
            popup="📍 Centroide",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

# Adicionar plugins úteis
folium.plugins.Fullscreen().add_to(m)
folium.plugins.MiniMap().add_to(m)

# Adicionar controle de camadas
folium.LayerControl().add_to(m)

# Exibir estatísticas do shapefile
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📊 Total de Geometrias", len(gdf))
with col2:
    if not gdf.empty and gdf.crs:
        st.metric("🌍 Sistema de Coordenadas", str(gdf.crs).split(':')[-1])
with col3:
    if not gdf.empty:
        area_ha = gdf.geometry.area.sum() / 10000  # Converter para hectares
        st.metric("📐 Área Total (ha)", f"{area_ha:.2f}")

# Exibir o mapa
st.markdown("<style>div.block-container{padding-top:0rem;padding-bottom:0rem;}</style>", unsafe_allow_html=True)
map_data = st_folium(m, width=None, height=700)

# Seção de informações adicionais
with st.expander("ℹ️ Informações Adicionais"):
    st.write("### 📋 Dados do Shapefile")
    if not gdf.empty:
        st.dataframe(gdf.drop(columns=['geometry']), use_container_width=True)
    
    st.write("### 🛠️ Funcionalidades Disponíveis")
    st.write("""
    - **Múltiplas camadas de base**: OpenStreetMap, Stamen Terrain, CartoDB, Satélite
    - **Visualização de shapefiles**: Suporte a polígonos e multipolígonos
    - **Popups informativos**: Exibição dos atributos do shapefile
    - **Controle de estilo**: Personalização de cores e opacidade
    - **Plugins úteis**: Tela cheia, minimapa
    - **Sistema de login**: Controle de acesso por usuário
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🗺️ WebGIS desenvolvido por Wdias Assessoria Rural e Engenharia</p>
        <p>Powered by Streamlit + Folium + GeoPandas</p>
    </div>
    """,
    unsafe_allow_html=True
) 