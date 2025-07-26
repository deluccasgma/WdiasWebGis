import streamlit as st
from streamlit_folium import st_folium
import folium
import json
import os
import numpy as np
import glob
import geopandas as gpd
from folium import plugins
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="WebGIS - Wdias Assessoria Rural",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para encontrar shapefiles
def encontrar_shapefiles():
    """Encontra todos os arquivos .shp no diretório atual"""
    arquivos = glob.glob("*.shp")
    if not arquivos:
        # Procura também em subdiretórios
        arquivos = glob.glob(os.path.join("**", "*.shp"), recursive=True)
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            background-size: cover;
            background-position: center;
        }
        .login-box {
            background: rgba(255,255,255,0.95);
            padding: 2.5rem;
            border-radius: 20px;
            max-width: 400px;
            margin: 100px auto 0 auto;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.18);
        }
        .login-title {
            text-align: center;
            color: #2c3e50;
            font-size: 2rem;
            margin-bottom: 1rem;
            font-weight: bold;
        }
        .login-subtitle {
            text-align: center;
            color: #27ae60;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🗺️ WebGIS</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Wdias Assessoria Rural e Engenharia</div>', unsafe_allow_html=True)
    
    usuario = st.text_input("👤 Usuário", placeholder="Digite seu usuário")
    senha = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Entrar", use_container_width=True):
            if usuario in usuarios and usuarios[usuario] == senha:
                st.session_state.autenticado = True
                st.session_state.usuario = usuario
                st.success(f"Bem-vindo, {usuario}!")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha incorretos.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# CSS personalizado para melhorar a aparência
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2c3e50, #3498db);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    .info-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stSelectbox > div > div {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🗺️ WebGIS - Sistema de Informações Geográficas</h1>
    <p>Wdias Assessoria Rural e Engenharia</p>
</div>
""", unsafe_allow_html=True)

# Mensagem especial para administradores
if st.session_state.get("usuario") in admins:
    st.sidebar.success("🔑 Você está logado como ADMINISTRADOR")

# Sidebar com controles
st.sidebar.title("⚙️ Controles do Mapa")

# Encontrar shapefiles disponíveis
shapefiles_disponiveis = encontrar_shapefiles()

if not shapefiles_disponiveis:
    st.error("❌ Nenhum arquivo shapefile encontrado no diretório!")
    st.stop()

# Seleção de shapefile
shapefile_selecionado = st.sidebar.selectbox(
    "📂 Selecionar Shapefile:",
    shapefiles_disponiveis,
    format_func=lambda x: os.path.basename(x)
)

# Carregar o shapefile selecionado
try:
    gdf = gpd.read_file(shapefile_selecionado)
    
    # Reprojetar para WGS84 se necessário
    if gdf.crs != 'EPSG:4326':
        gdf = gdf.to_crs('EPSG:4326')
    
    geojson_data = gdf.__geo_interface__
    
except Exception as e:
    st.error(f"❌ Erro ao carregar o shapefile: {e}")
    st.stop()

# Informações do shapefile
st.sidebar.markdown("### 📊 Informações do Shapefile")
st.sidebar.info(f"""
**Arquivo:** {os.path.basename(shapefile_selecionado)}
**Número de features:** {len(gdf)}
**Sistema de coordenadas:** {gdf.crs}
**Colunas:** {len(gdf.columns)-1}
""")

# Controles de visualização
st.sidebar.markdown("### 🎨 Opções de Visualização")
show_shapefile = st.sidebar.checkbox("Exibir Shapefile", value=True)
show_labels = st.sidebar.checkbox("Exibir Rótulos", value=False)
opacity = st.sidebar.slider("Opacidade", 0.1, 1.0, 0.7, 0.1)

# Seleção de campo para colorir
if len(gdf.columns) > 1:
    campos_numericos = gdf.select_dtypes(include=[np.number]).columns.tolist()
    if campos_numericos:
        campo_cor = st.sidebar.selectbox(
            "🎨 Colorir por campo:",
            ["Nenhum"] + campos_numericos
        )
    else:
        campo_cor = "Nenhum"
else:
    campo_cor = "Nenhum"

# Função para calcular centroide
def calcular_centroide_bounds(gdf):
    """Calcula o centroide baseado nos bounds do GeoDataFrame"""
    bounds = gdf.total_bounds
    center_lat = (bounds[1] + bounds[3]) / 2
    center_lon = (bounds[0] + bounds[2]) / 2
    return [center_lat, center_lon]

# Calcular centroide para centralizar o mapa
center = calcular_centroide_bounds(gdf)

# Criar o mapa folium
m = folium.Map(
    location=center, 
    zoom_start=12, 
    control_scale=True,
    tiles=None
)

# Adicionar diferentes camadas de base
folium.TileLayer("OpenStreetMap", name="🗺️ OpenStreetMap").add_to(m)
folium.TileLayer(
    "CartoDB positron",
    name="🏙️ CartoDB Positron",
    attr="©OpenStreetMap, ©CartoDB"
).add_to(m)
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    name="🛰️ Satélite (Esri)",
    attr="Tiles © Esri"
).add_to(m)
folium.TileLayer(
    "Stamen Terrain",
    name="🏔️ Terreno",
    attr="Map tiles by Stamen Design"
).add_to(m)

# Adicionar GeoJSON como camada
if show_shapefile:
    # Preparar popup com informações
    popup_fields = [col for col in gdf.columns if col != 'geometry']
    
    # Função para criar popup personalizado
    def create_popup(row):
        popup_html = "<div style='font-family: Arial; font-size: 12px;'>"
        popup_html += f"<h4 style='color: #2c3e50; margin-bottom: 10px;'>📍 Informações da Feature</h4>"
        
        for field in popup_fields:
            value = row[field]
            if pd.isna(value):
                value = "N/A"
            elif isinstance(value, float):
                if field.lower() in ['area', 'área']:
                    value = f"{value:.2f} ha"
                else:
                    value = f"{value:.2f}"
            
            popup_html += f"<b>{field}:</b> {value}<br>"
        
        # Calcular área se for polígono
        if hasattr(row.geometry, 'area'):
            area_m2 = row.geometry.area * 111319.9**2  # Aproximação para metros quadrados
            area_ha = area_m2 / 10000
            popup_html += f"<b>Área calculada:</b> {area_ha:.2f} ha<br>"
        
        popup_html += "</div>"
        return popup_html
    
    # Estilo baseado no campo selecionado
    if campo_cor != "Nenhum" and campo_cor in gdf.columns:
        # Normalizar valores para cores
        valores = gdf[campo_cor].fillna(0)
        min_val, max_val = valores.min(), valores.max()
        
        def style_function(feature):
            valor = feature['properties'].get(campo_cor, 0)
            if max_val > min_val:
                normalized = (valor - min_val) / (max_val - min_val)
                color_intensity = int(255 * (1 - normalized))
                color = f'#{255:02x}{color_intensity:02x}{color_intensity:02x}'
            else:
                color = '#3498db'
            
            return {
                'fillColor': color,
                'color': '#2c3e50',
                'weight': 2,
                'fillOpacity': opacity,
                'opacity': 0.8
            }
    else:
        def style_function(feature):
            return {
                'fillColor': '#3498db',
                'color': '#2c3e50',
                'weight': 2,
                'fillOpacity': opacity,
                'opacity': 0.8
            }
    
    # Adicionar camada com popups personalizados
    for idx, row in gdf.iterrows():
        popup_content = create_popup(row)
        
        folium.GeoJson(
            row.geometry.__geo_interface__,
            style_function=lambda x, row=row: style_function({'properties': row.to_dict()}),
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=f"Feature {idx + 1}"
        ).add_to(m)

# Adicionar plugins úteis
plugins.Fullscreen().add_to(m)
plugins.MeasureControl().add_to(m)
plugins.LocateControl().add_to(m)

# Adicionar controle de camadas
folium.LayerControl(position='topright').add_to(m)

# Layout principal
col1, col2 = st.columns([3, 1])

with col1:
    # Exibir o mapa
    map_data = st_folium(m, width=None, height=600, returned_objects=["last_clicked"])

with col2:
    st.markdown("### 📊 Estatísticas")
    
    # Métricas gerais
    st.markdown(f"""
    <div class="metric-card">
        <h3>{len(gdf)}</h3>
        <p>Features Total</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'area' in gdf.columns:
        area_total = gdf['area'].sum()
        st.markdown(f"""
        <div class="metric-card">
            <h3>{area_total:.2f} ha</h3>
            <p>Área Total</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Informações da feature clicada
    if map_data['last_clicked']:
        st.markdown("### 🎯 Feature Selecionada")
        lat, lon = map_data['last_clicked']['lat'], map_data['last_clicked']['lng']
        st.write(f"**Coordenadas:** {lat:.6f}, {lon:.6f}")
    
    # Tabela com dados
    st.markdown("### 📋 Dados das Features")
    if st.button("📥 Mostrar Tabela"):
        st.dataframe(gdf.drop('geometry', axis=1), use_container_width=True)

# Informações adicionais no rodapé
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h4>🛠️ Ferramentas Disponíveis</h4>
        <ul>
            <li>Medição de distâncias e áreas</li>
            <li>Localização GPS</li>
            <li>Tela cheia</li>
            <li>Múltiplas camadas de base</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h4>📍 Informações do Sistema</h4>
        <ul>
            <li>Sistema de coordenadas: WGS84</li>
            <li>Formato suportado: Shapefile</li>
            <li>Visualização interativa</li>
            <li>Popups informativos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="info-card">
        <h4>👤 Sessão Atual</h4>
        <ul>
            <li>Usuário: {st.session_state.usuario}</li>
            <li>Arquivo: {os.path.basename(shapefile_selecionado)}</li>
            <li>Features: {len(gdf)}</li>
            <li>Status: ✅ Conectado</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Botão de logout
if st.sidebar.button("🚪 Sair", use_container_width=True):
    st.session_state.autenticado = False
    st.rerun() 