#!/bin/bash

echo "🚀 Deploy automático para Streamlit Cloud"
echo "=========================================="

# Verificar se estamos no diretório correto
if [ ! -f "app_robust.py" ]; then
    echo "❌ Erro: app_robust.py não encontrado!"
    echo "   Certifique-se de estar no diretório correto."
    exit 1
fi

# Verificar se git está configurado
if ! git config --get user.name > /dev/null 2>&1; then
    echo "❌ Git não está configurado!"
    echo "   Configure com: git config --global user.name 'Seu Nome'"
    echo "   Configure com: git config --global user.email 'seu@email.com'"
    exit 1
fi

# Adicionar todos os arquivos
echo "📦 Adicionando arquivos..."
git add .

# Fazer commit
echo "💾 Fazendo commit..."
git commit -m "Deploy automático - Versão robusta para Streamlit Cloud"

# Fazer push
echo "🚀 Fazendo push para GitHub..."
git push origin main

echo ""
echo "✅ Deploy concluído!"
echo ""
echo "📋 Próximos passos no Streamlit Cloud:"
echo "1. Vá para: https://share.streamlit.io"
echo "2. Clique em 'Manage app'"
echo "3. Vá em 'Settings'"
echo "4. Mude 'Main file path' para: app_robust.py"
echo "5. Clique em 'Save'"
echo ""
echo "🌐 Seu app estará disponível em alguns minutos!"