# 🚀 Guia de Deploy - WebGIS Wdias

Este guia contém instruções detalhadas para fazer o deploy do WebGIS em diferentes plataformas.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Git
- Acesso à internet para download de dependências

## 🏠 Deploy Local

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/WdiasWebGis.git
cd WdiasWebGis
```

### 2. Instalação rápida (Linux/Mac)
```bash
chmod +x run.sh
./run.sh
```

### 3. Instalação manual
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run app.py
```

### 4. Acessar a aplicação
Abra o navegador e acesse: `http://localhost:8501`

## ☁️ Deploy na Nuvem

### Streamlit Cloud (Recomendado)

1. **Faça push para o GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Acesse [share.streamlit.io](https://share.streamlit.io)**

3. **Conecte seu repositório GitHub**

4. **Configure o deploy:**
   - **Main file path**: `app.py`
   - **Python version**: 3.9
   - **Requirements file**: `requirements.txt`

5. **Clique em "Deploy"**

### Heroku

1. **Instale o Heroku CLI**

2. **Crie um arquivo `Procfile`:**
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

3. **Deploy:**
```bash
heroku create wdias-webgis
git push heroku main
heroku open
```

### Docker

1. **Build da imagem:**
```bash
docker build -t wdias-webgis .
```

2. **Executar container:**
```bash
docker run -p 8501:8501 wdias-webgis
```

3. **Usando Docker Compose:**
```bash
docker-compose up -d
```

### Google Cloud Platform

1. **Instale o Google Cloud SDK**

2. **Deploy no App Engine:**
```bash
gcloud app deploy app.yaml
```

3. **Crie um arquivo `app.yaml`:**
```yaml
runtime: python39
entrypoint: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

env_variables:
  STREAMLIT_SERVER_PORT: 8080
  STREAMLIT_SERVER_ADDRESS: 0.0.0.0
```

### AWS

1. **Deploy no Elastic Beanstalk:**
```bash
eb init
eb create wdias-webgis
eb deploy
```

2. **Ou usando AWS Lambda + API Gateway** (mais complexo)

## 🔧 Configurações Avançadas

### Variáveis de Ambiente

Crie um arquivo `.env`:
```env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Configuração do Nginx (Produção)

```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

### SSL/HTTPS

1. **Usando Let's Encrypt:**
```bash
sudo certbot --nginx -d seu-dominio.com
```

2. **Ou configure SSL no seu provedor de nuvem**

## 📊 Monitoramento

### Logs
```bash
# Streamlit Cloud: Disponível no dashboard
# Heroku: heroku logs --tail
# Docker: docker logs container_name
# Local: streamlit run app.py --logger.level debug
```

### Métricas
- **Uptime**: Configure alertas no seu provedor
- **Performance**: Monitore tempo de resposta
- **Erros**: Configure logging de erros

## 🔒 Segurança

### Autenticação
- O sistema já possui login integrado
- Considere adicionar autenticação externa (OAuth, SAML)
- Use HTTPS em produção

### Dados
- Backup regular dos shapefiles
- Versionamento dos dados
- Controle de acesso por usuário

## 🐛 Solução de Problemas

### Erro: "No module named 'geopandas'"
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Erro: "Port already in use"
```bash
# Encontre o processo
lsof -i :8501
# Mate o processo
kill -9 PID
```

### Erro: "Permission denied"
```bash
chmod +x run.sh
chmod +x app.py
```

### Erro: "Shapefile not found"
- Verifique se todos os arquivos .shp, .dbf, .prj, .shx estão presentes
- Confirme o caminho no código

## 📞 Suporte

Para suporte técnico:
- **Email**: gilmar@wdias.eng.br
- **Issues**: Abra uma issue no GitHub
- **Documentação**: Consulte o README.md

## 🔄 Atualizações

Para atualizar o sistema:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
streamlit run app.py
```

---

**Desenvolvido por Wdias Assessoria Rural e Engenharia**