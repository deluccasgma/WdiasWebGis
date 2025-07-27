#!/usr/bin/env python3
"""
WebGIS - Versão otimizada para Render
"""
import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import os

# Configuração da página
st.set_page_config(
    page_title="WebGIS - Wdias",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
    }
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        width: 100%;
        background-color: #1f4e79;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #0d2b4a;
    }
</style>
""", unsafe_allow_html=True)

# Dados de exemplo (GeoJSON)
sample_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Propriedade 1",
                "area": "150 hectares",
                "tipo": "Agricultura",
                "proprietario": "João Silva"
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
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Propriedade 2",
                "area": "200 hectares",
                "tipo": "Pecuária",
                "proprietario": "Maria Santos"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-46.6400, -23.5490],
                    [-46.6400, -23.5485],
                    [-46.6390, -23.5485],
                    [-46.6390, -23.5490],
                    [-46.6400, -23.5490]
                ]]
            }
        }
    ]
}

# Sistema de autenticação simples
def check_password():
    """Retorna `True` se a senha correta for inserida."""
    def password_entered():
        if st.session_state["password"] == "admin123":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown('<h1 class="main-header">🗺️ WebGIS - Wdias</h1>', unsafe_allow_html=True)
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.text_input("Senha", type="password", on_change=password_entered, key="password")
        st.markdown('</div>', unsafe_allow_html=True)
        return False
    elif not st.session_state["password_correct"]:
        st.markdown('<h1 class="main-header">🗺️ WebGIS - Wdias</h1>', unsafe_allow_html=True)
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.text_input("Senha", type="password", on_change=password_entered, key="password")
        st.error("😕 Senha incorreta")
        st.markdown('</div>', unsafe_allow_html=True)
        return False
    else:
        return True

def main():
    """Função principal do aplicativo."""
    if check_password():
        # Interface principal
        st.markdown('<h1 class="main-header">🗺️ WebGIS - Wdias</h1>', unsafe_allow_html=True)
        
        # Sidebar
        with st.sidebar:
            st.header("📊 Informações")
            st.info("**WebGIS - Wdias Assessoria Rural**")
            st.write("Sistema de Informações Geográficas")
            
            st.header("🗺️ Dados")
            st.write(f"**Propriedades:** {len(sample_geojson['features'])}")
            st.write("**Tipo:** Shapefiles convertidos")
            
            st.header("🔧 Opções")
            show_popups = st.checkbox("Mostrar Popups", value=True)
            show_measure = st.checkbox("Ferramenta de Medição", value=True)
            
            st.header("👤 Usuário")
            st.success("✅ Logado como Admin")
            if st.button("🚪 Logout"):
                st.session_state["password_correct"] = False
                st.rerun()
        
        # Mapa principal
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader("🗺️ Mapa Interativo")
            
            # Criar mapa
            try:
                # Calcular centroide aproximado
                coords = sample_geojson['features'][0]['geometry']['coordinates'][0]
                center_lat = sum(coord[1] for coord in coords) / len(coords)
                center_lon = sum(coord[0] for coord in coords) / len(coords)
                
                m = folium.Map(
                    location=[center_lat, center_lon],
                    zoom_start=15,
                    tiles=None
                )
                
                # Adicionar camadas de base
                folium.TileLayer(
                    tiles='OpenStreetMap',
                    name='🗺️ OpenStreetMap',
                    overlay=False,
                    control=True
                ).add_to(m)
                
                folium.TileLayer(
                    tiles='Stamen Terrain',
                    name='🏔️ Stamen Terrain',
                    overlay=False,
                    control=True
                ).add_to(m)
                
                folium.TileLayer(
                    tiles='CartoDB positron',
                    name='📊 CartoDB Positron',
                    overlay=False,
                    control=True
                ).add_to(m)
                
                folium.TileLayer(
                    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    name='🛰️ Esri Satellite',
                    overlay=False,
                    control=True,
                    attr='Esri'
                ).add_to(m)
                
                # Adicionar dados GeoJSON
                folium.GeoJson(
                    sample_geojson,
                    name="🏠 Propriedades",
                    style_function=lambda feature: {
                        'fillColor': '#FF6B6B',
                        'color': '#1f4e79',
                        'weight': 2,
                        'fillOpacity': 0.7
                    },
                    popup=folium.GeoJsonPopup(
                        fields=['name', 'area', 'tipo', 'proprietario'],
                        aliases=['Nome:', 'Área:', 'Tipo:', 'Proprietário:'],
                        localize=True,
                        labels=True,
                        style="background-color: yellow;"
                    ) if show_popups else None,
                    tooltip=folium.GeoJsonTooltip(
                        fields=['name', 'area'],
                        aliases=['Nome:', 'Área:'],
                        localize=True,
                        sticky=False,
                        labels=True,
                        style="""
                            background-color: white;
                            border: 2px solid black;
                            border-radius: 3px;
                            box-shadow: 3px;
                        """
                    )
                ).add_to(m)
                
                # Adicionar plugins
                if show_measure:
                    folium.plugins.MeasureControl(
                        position='topleft',
                        primary_length_unit='meters',
                        secondary_length_unit='kilometers',
                        primary_area_unit='sqmeters',
                        secondary_area_unit='acres'
                    ).add_to(m)
                
                folium.plugins.Fullscreen(
                    position='topleft',
                    title='Expand me',
                    title_cancel='Exit me',
                    force_separate_button=True
                ).add_to(m)
                
                folium.plugins.MousePosition().add_to(m)
                
                # Controle de camadas
                folium.LayerControl(
                    position='topright',
                    collapsed=False
                ).add_to(m)
                
                # Exibir mapa
                st_folium(m, width=700, height=500)
                
            except Exception as e:
                st.error(f"Erro ao carregar o mapa: {str(e)}")
                st.info("Tentando carregar mapa básico...")
                
                # Mapa de fallback
                m = folium.Map(location=[-23.5489, -46.6388], zoom_start=10)
                st_folium(m, width=700, height=500)
        
        with col2:
            st.subheader("📊 Estatísticas")
            st.metric("Propriedades", len(sample_geojson['features']))
            st.metric("Total de Área", "350 hectares")
            st.metric("Tipos", "2")
            
            st.subheader("ℹ️ Informações")
            st.info("""
            **WebGIS - Wdias Assessoria Rural**
            
            Sistema desenvolvido para:
            - 📍 Visualização de propriedades
            - 📊 Análise geográfica
            - 🗺️ Mapeamento rural
            - 📱 Acesso mobile
            
            **Contato:**
            📧 contato@wdias.com.br
            📞 (11) 99999-9999
            """)

if __name__ == "__main__":
    main()