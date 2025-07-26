#!/bin/bash

# Script de inicialização do WebGIS
echo "🗺️ Iniciando WebGIS - Wdias Assessoria Rural e Engenharia"
echo "=================================================="

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Por favor, instale o Python 3.8 ou superior."
    exit 1
fi

# Verificar se o pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Por favor, instale o pip."
    exit 1
fi

# Instalar dependências se necessário
echo "📦 Verificando dependências..."
pip3 install -r requirements.txt

# Verificar se há shapefiles
if [ ! -f *.shp ]; then
    echo "⚠️  Nenhum arquivo .shp encontrado no diretório atual."
    echo "   Certifique-se de que os arquivos shapefile estão presentes."
fi

# Iniciar a aplicação
echo "🚀 Iniciando aplicação Streamlit..."
echo "📱 Acesse: http://localhost:8501"
echo "🛑 Para parar a aplicação, pressione Ctrl+C"
echo ""

streamlit run app.py --server.port=8501 --server.address=0.0.0.0