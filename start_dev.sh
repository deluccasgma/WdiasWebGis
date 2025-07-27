#!/bin/bash

echo "🚀 Iniciando ambiente de desenvolvimento WebGIS"
echo "================================================"

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado!"
    exit 1
fi

# Verificar se as dependências estão instaladas
echo "📦 Verificando dependências..."
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "⚠️  Streamlit não encontrado. Instalando..."
    pip install -r requirements_simple.txt
fi

# Parar processos existentes
echo "🛑 Parando processos existentes..."
pkill -f streamlit 2>/dev/null
pkill -f "python.*server.py" 2>/dev/null

# Iniciar Streamlit em background
echo "🗺️  Iniciando Streamlit..."
streamlit run app_robust.py --server.port=8501 --server.address=0.0.0.0 &
STREAMLIT_PID=$!

# Aguardar Streamlit inicializar
echo "⏳ Aguardando Streamlit inicializar..."
sleep 5

# Verificar se Streamlit está rodando
if curl -s http://localhost:8501 > /dev/null; then
    echo "✅ Streamlit iniciado com sucesso!"
else
    echo "❌ Erro ao iniciar Streamlit"
    exit 1
fi

# Iniciar servidor HTTP para o site
echo "🌐 Iniciando servidor HTTP..."
python3 server.py &
SERVER_PID=$!

echo ""
echo "🎉 Ambiente de desenvolvimento iniciado!"
echo ""
echo "📱 URLs de acesso:"
echo "   🌐 Site principal: http://localhost:8000"
echo "   🗺️  WebGIS direto: http://localhost:8501"
echo "   📱 IP Local: http://172.30.0.2:8000"
echo ""
echo "🔧 Para parar tudo:"
echo "   pkill -f streamlit"
echo "   pkill -f server.py"
echo ""
echo "⏹️  Pressione Ctrl+C para parar este script"

# Função para limpeza ao sair
cleanup() {
    echo ""
    echo "🛑 Parando serviços..."
    kill $STREAMLIT_PID 2>/dev/null
    kill $SERVER_PID 2>/dev/null
    pkill -f streamlit 2>/dev/null
    pkill -f "python.*server.py" 2>/dev/null
    echo "✅ Serviços parados"
    exit 0
}

# Capturar Ctrl+C
trap cleanup SIGINT

# Manter script rodando
wait