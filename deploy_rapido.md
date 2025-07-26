# 📱 Deploy Rápido para Acesso Mobile

## ⚡ Método Mais Rápido

### 1. Deploy no Streamlit Cloud (5 minutos)

```bash
# 1. Faça commit e push
git add .
git commit -m "WebGIS mobile ready"
git push origin main

# 2. Acesse: https://share.streamlit.io
# 3. Conecte seu GitHub
# 4. Configure:
#    - Main file: app.py
#    - Python version: 3.9
# 5. Deploy!
```

### 2. Acesso Mobile
- Copie o link fornecido pelo Streamlit Cloud
- Cole no navegador do celular
- Pronto! 🎉

## 🔧 Deploy Local para Rede WiFi

### 1. Execute no Computador
```bash
streamlit run app.py --server.address 0.0.0.0
```

### 2. Descubra o IP
```bash
# Linux/Mac
hostname -I

# Windows
ipconfig | findstr IPv4
```

### 3. Acesse no Celular
```
http://SEU_IP:8501
```

## 📱 Teste Rápido

1. **Abra o navegador do celular**
2. **Acesse o link do WebGIS**
3. **Faça login** com qualquer usuário
4. **Teste as funcionalidades**:
   - Zoom no mapa
   - Toque nos polígonos
   - Troque camadas de base
   - Use a sidebar

## 🎯 Funcionalidades Mobile

- ✅ **Login touch-friendly**
- ✅ **Mapa responsivo**
- ✅ **Zoom e pan**
- ✅ **Popups informativos**
- ✅ **Múltiplas camadas**
- ✅ **Tela cheia**
- ✅ **Minimapa**

## 🚨 Solução de Problemas

### "Não consigo acessar"
- Verifique se está na mesma rede WiFi
- Confirme o IP do computador
- Teste no navegador do computador primeiro

### "Mapa não carrega"
- Verifique a conexão com internet
- Recarregue a página
- Limpe cache do navegador

### "Lento no celular"
- Use WiFi ao invés de dados móveis
- Feche outros apps
- Use modo tela cheia

## 📞 Suporte Mobile

Se tiver problemas:
- **Email**: gilmar@wdias.eng.br
- **Teste**: Primeiro no computador
- **Verifique**: Conexão e IP

---

**WebGIS Mobile Ready! 📱🗺️**