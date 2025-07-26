# 🚀 Guia de Deploy - WebGIS Wdias

Este guia explica como fazer o deploy do WebGIS em diferentes ambientes.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- GDAL instalado no sistema
- Acesso ao servidor/container

## 🐳 Deploy com Docker (Recomendado)

### 1. Criar Dockerfile

```dockerfile
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir variáveis de ambiente
ENV PYTHONPATH=/app
ENV GDAL_DATA=/usr/share/gdal

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt packages.txt ./

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 8501

# Comando para executar a aplicação
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Construir e executar

```bash
# Construir imagem
docker build -t webgis-wdias .

# Executar container
docker run -d -p 8501:8501 --name webgis webgis-wdias
```

## ☁️ Deploy no Streamlit Cloud

1. Faça push do código para o GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório GitHub
4. Configure o arquivo principal como `app.py`
5. Deploy automático!

## 🖥️ Deploy em Servidor Linux

### 1. Instalar dependências do sistema

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install -y python3 python3-pip python3-venv gdal-bin libgdal-dev

# CentOS/RHEL
sudo yum install -y python3 python3-pip gdal-devel
```

### 2. Configurar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Executar aplicação

```bash
# Desenvolvimento
streamlit run app.py

# Produção (com nohup)
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 > app.log 2>&1 &
```

## 🔧 Configuração com Systemd

### 1. Criar arquivo de serviço

```bash
sudo nano /etc/systemd/system/webgis.service
```

### 2. Conteúdo do arquivo

```ini
[Unit]
Description=WebGIS Wdias
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/path/to/your/app
Environment=PATH=/path/to/your/app/venv/bin
ExecStart=/path/to/your/app/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

### 3. Ativar serviço

```bash
sudo systemctl daemon-reload
sudo systemctl enable webgis
sudo systemctl start webgis
sudo systemctl status webgis
```

## 🌐 Configuração com Nginx (Opcional)

### 1. Instalar Nginx

```bash
sudo apt install nginx
```

### 2. Configurar proxy reverso

```bash
sudo nano /etc/nginx/sites-available/webgis
```

### 3. Conteúdo da configuração

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

### 4. Ativar configuração

```bash
sudo ln -s /etc/nginx/sites-available/webgis /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 Configurações de Segurança

### 1. Firewall

```bash
# Permitir apenas porta 80/443
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

### 2. SSL/HTTPS (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d seu-dominio.com
```

## 📊 Monitoramento

### 1. Logs da aplicação

```bash
# Ver logs em tempo real
tail -f app.log

# Ver logs do systemd
sudo journalctl -u webgis -f
```

### 2. Status do serviço

```bash
sudo systemctl status webgis
```

## 🔄 Atualizações

### 1. Atualizar código

```bash
git pull origin main
sudo systemctl restart webgis
```

### 2. Atualizar dependências

```bash
source venv/bin/activate
pip install -r requirements.txt --upgrade
sudo systemctl restart webgis
```

## 🆘 Troubleshooting

### Problemas comuns:

1. **Erro de GDAL**: Instale as dependências do sistema
2. **Porta ocupada**: Verifique se não há outro processo na porta 8501
3. **Permissões**: Certifique-se de que o usuário tem permissões adequadas
4. **Memória**: Aumente a memória disponível se necessário

### Comandos úteis:

```bash
# Verificar se a aplicação está rodando
ps aux | grep streamlit

# Verificar portas em uso
netstat -tlnp | grep 8501

# Reiniciar aplicação
sudo systemctl restart webgis
```

---

Para suporte adicional, entre em contato: gilmar@wdias.eng.br