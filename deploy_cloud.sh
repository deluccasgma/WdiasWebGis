#!/bin/bash

echo "🚀 Deploy Rápido para Acesso Mobile"
echo "=================================="

# Verificar se git está configurado
if ! git config --get user.name > /dev/null 2>&1; then
    echo "❌ Git não está configurado. Configure primeiro:"
    echo "git config --global user.name 'Seu Nome'"
    echo "git config --global user.email 'seu@email.com'"
    exit 1
fi

# Verificar se tem repositório remoto
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ Repositório remoto não configurado."
    echo "Crie um repositório no GitHub e conecte:"
    echo "git remote add origin https://github.com/seu-usuario/WdiasWebGis.git"
    exit 1
fi

echo "✅ Git configurado"

# Fazer commit e push
echo "📤 Fazendo push para GitHub..."
git add .
git commit -m "WebGIS mobile ready - $(date)"
git push origin main

echo ""
echo "🎉 Push realizado com sucesso!"
echo ""
echo "📱 Agora faça o deploy na nuvem:"
echo ""
echo "1️⃣ Acesse: https://share.streamlit.io"
echo "2️⃣ Conecte seu GitHub"
echo "3️⃣ Selecione o repositório: WdiasWebGis"
echo "4️⃣ Configure:"
echo "   - Main file: app.py"
echo "   - Python version: 3.9"
echo "5️⃣ Clique em 'Deploy'"
echo ""
echo "📱 Após o deploy, copie o link e acesse no celular!"
echo ""
echo "🔗 Links úteis:"
echo "- Streamlit Cloud: https://share.streamlit.io"
echo "- Heroku: https://heroku.com"
echo "- Vercel: https://vercel.com"