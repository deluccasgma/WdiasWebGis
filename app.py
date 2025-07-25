import streamlit as st
from streamlit_folium import st_folium
import folium
import json
import os
import numpy as np
import glob

# Procurar automaticamente o primeiro arquivo .geojson na pasta Shapefile
def encontrar_geojson():
    arquivos = glob.glob(os.path.join("Shapefile", "*.geojson"))
    if arquivos:
        return arquivos[0]
    else:
        return None

geojson_path = encontrar_geojson()

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
    st.title("Login")
    st.markdown('<div style="text-align:center;font-size:1.1rem;margin-bottom:1rem;color:#2e7d32;font-weight:bold;">Bem Vindo ao WebGis- Wdias Assesoria Rural e Engenharia</div>', unsafe_allow_html=True)
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario] == senha:
            st.session_state.autenticado = True
            st.session_state.usuario = usuario
            st.success(f"Bem-vindo, {usuario}!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# Mensagem especial para administradores
if st.session_state.get("usuario") in admins:
    st.sidebar.info("Você está logado como ADMINISTRADOR.")

st.set_page_config(layout="wide")

# Sidebar para exibir/ocultar o shapefile
st.sidebar.title("Opções do Mapa")
show_shapefile = st.sidebar.checkbox("Exibir Shapefile", value=True)

# Carregar o GeoJSON
try:
    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)
except Exception as e:
    st.error(f"Erro ao carregar o arquivo GeoJSON: {e}")
    st.stop()

# Calcular centroide do polígono
def calcular_centroide(coords):
    # Suporta apenas Polygon (não MultiPolygon)
    x = [p[0] for p in coords[0]]
    y = [p[1] for p in coords[0]]
    area = 0.0
    cx = 0.0
    cy = 0.0
    n = len(coords[0]) - 1  # último ponto é igual ao primeiro
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

# Calcular centroide para centralizar o mapa
if geojson_data["features"]:
    geometry = geojson_data["features"][0]["geometry"]
    coords = geometry["coordinates"]
    if geometry["type"] == "Polygon":
        center = calcular_centroide(coords)
    elif geometry["type"] == "MultiPolygon":
        # Pega o primeiro polígono do multipolígono
        center = calcular_centroide(coords[0])
    else:
        center = [0, 0]
else:
    center = [0, 0]

# Criar o mapa folium
m = folium.Map(location=center, zoom_start=16, control_scale=True)

# Adicionar mapas de fundo
folium.TileLayer("OpenStreetMap", name="OpenStreetMap").add_to(m)
folium.TileLayer(
    "Stamen Terrain",
    name="Stamen Terrain",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors"
).add_to(m)
folium.TileLayer(
    "CartoDB positron",
    name="CartoDB Positron",
    attr="©OpenStreetMap, ©CartoDB"
).add_to(m)
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    name="Satélite (Esri)",
    attr="Tiles © Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
).add_to(m)

# Adicionar GeoJSON como camada
if show_shapefile:
    folium.GeoJson(
        geojson_data,
        name="Shapefile",
        popup=folium.GeoJsonPopup(fields=list(geojson_data["features"][0]["properties"].keys()))
    ).add_to(m)

# Adicionar controle de camadas
folium.LayerControl().add_to(m)

# Exibir o mapa no Streamlit
st.markdown("<style>div.block-container{padding-top:0rem;padding-bottom:0rem;}</style>", unsafe_allow_html=True)
st_folium(m, width=None, height=1100) 