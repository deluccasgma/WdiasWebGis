#!/usr/bin/env bash
# Script de build para Render

echo "🚀 Iniciando build no Render..."

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements_simple.txt

# Verificar se tudo foi instalado
echo "✅ Dependências instaladas:"
pip list

echo "🎉 Build concluído!"