#!/bin/bash

echo "🗺️ Iniciando WebGIS - Wdias Assessoria Rural e Engenharia"
echo "=================================================="

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não está instalado. Por favor, instale Python 3.8 ou superior."
    exit 1
fi

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não está instalado. Por favor, instale pip."
    exit 1
fi

echo "✅ Python e pip encontrados"

# Instalar dependências se necessário
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

echo "📥 Instalando dependências..."
pip install -r requirements.txt

echo "🚀 Iniciando aplicação..."
echo "🌐 Acesse: http://localhost:8501"
echo "⏹️  Para parar, pressione Ctrl+C"
echo ""

streamlit run app.py