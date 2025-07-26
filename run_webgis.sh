#!/bin/bash

echo "🗺️  Iniciando WebGIS - Wdias Assessoria Rural e Engenharia"
echo "=========================================================="

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "⚠️  Ambiente virtual não encontrado. Criando..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Verificar se existem shapefiles
shapefiles=$(find . -name "*.shp" | head -5)
if [ -z "$shapefiles" ]; then
    echo "⚠️  Nenhum shapefile encontrado no diretório atual!"
    echo "   Por favor, adicione arquivos .shp ao diretório para usar o WebGIS."
else
    echo "✅ Shapefiles encontrados:"
    find . -name "*.shp" -exec basename {} \; | head -5
fi

echo ""
echo "🚀 Iniciando aplicação WebGIS..."
echo "   Acesse: http://localhost:8501"
echo "   Para parar: Ctrl+C"
echo ""

# Executar aplicação
streamlit run app.py