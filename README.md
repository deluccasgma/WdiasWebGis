# 🌐 WebGIS - Sistema de Informação Geográfica Web

Um sistema completo de WebGIS desenvolvido em Python com Streamlit e Folium para visualização e análise de dados geográficos.

## 🚀 Deploy Rápido

### **Render (Recomendado)**
1. **Fork este repositório** ou clone para sua conta
2. **Acesse:** [render.com](https://render.com)
3. **Clique em "New +" → "Web Service"**
4. **Conecte seu GitHub** e selecione este repositório
5. **Configure:**
   - **Name:** `webgis-wdias`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements_simple.txt`
   - **Start Command:** `streamlit run app_robust.py --server.port=$PORT --server.address=0.0.0.0`
6. **Clique em "Create Web Service"**
7. **Aguarde o deploy** (2-3 minutos)
8. **Acesse:** `https://webgis-wdias.onrender.com`

### **Streamlit Cloud**
1. **Acesse:** [share.streamlit.io](https://share.streamlit.io)
2. **Conecte seu GitHub**
3. **Configure:**
   - **Repository:** seu-repositorio
   - **Branch:** main
   - **Main file path:** `app_robust.py`
4. **Deploy automático**

### **Railway**
1. **Acesse:** [railway.app](https://railway.app)
2. **Conecte GitHub**
3. **Deploy automático**

## 📱 Acesso Mobile

Após o deploy, você pode acessar de qualquer dispositivo:
- **📱 Celular:** Use o link gerado pelo Render
- **💻 Computador:** Mesmo link funciona em desktop
- **🌐 Compartilhar:** Envie o link para amigos/colegas

# 🗺️ WebGIS - Wdias Assessoria Rural e Engenharia

Sistema de Informações Geográficas Web desenvolvido para visualização e análise de dados geoespaciais.

## 📋 Descrição

Este WebGIS permite visualizar shapefiles de forma interativa através de uma interface web moderna e responsiva. O sistema inclui:

- 🔐 Sistema de autenticação
- 🗺️ Múltiplas camadas de mapas base
- 📊 Visualização de shapefiles
- 📏 Ferramentas de medição
- 💬 Popups informativos
- 🖥️ Modo tela cheia
- 📱 Interface responsiva

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- GDAL instalado no sistema

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-seu-repositorio>
cd <nome-do-repositorio>
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. Acesse no navegador:
```
http://localhost:8501
```

## 👥 Usuários do Sistema

### Administradores
- **admin** / senhaadm
- **deluccasgma@gmail.com** / Lg1401@@

### Usuários Comuns
- **usuario1** / senha1
- **usuario2** / senha2
- **gilmar@wdias.eng.br** / 123456

## 📁 Estrutura do Projeto

```
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── packages.txt          # Dependências do sistema
├── README.md             # Documentação
├── ÁREA_DO_IMOVEL.shp    # Shapefile principal
├── ÁREA_DO_IMOVEL.dbf    # Atributos do shapefile
├── ÁREA_DO_IMOVEL.prj    # Sistema de coordenadas
└── ÁREA_DO_IMOVEL.shx    # Índice espacial
```

## 🗺️ Funcionalidades

### Mapas Base Disponíveis
- 🗺️ OpenStreetMap
- 🏔️ Stamen Terrain
- 📰 CartoDB Positron
- 🛰️ Satélite (Esri)

### Ferramentas
- 📏 Medição de distâncias e áreas
- 🖱️ Posição do mouse
- 🖥️ Modo tela cheia
- 🎛️ Controle de camadas
- 💬 Popups informativos

## 🔧 Configuração

### Adicionando Novos Shapefiles

1. Coloque os arquivos `.shp`, `.dbf`, `.prj`, `.shx` na raiz do projeto
2. O sistema detectará automaticamente o primeiro shapefile encontrado

### Personalizando Usuários

Edite o dicionário `usuarios` no arquivo `app.py`:

```python
usuarios = {
    "novo_usuario": "nova_senha",
    # ... outros usuários
}
```

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework web para Python
- **Folium**: Biblioteca para criação de mapas interativos
- **GeoPandas**: Manipulação de dados geoespaciais
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica

## 📞 Contato

**Wdias Assessoria Rural e Engenharia**
- 📧 Email: gilmar@wdias.eng.br
- 🏢 Empresa especializada em assessoria rural e engenharia

## 📄 Licença

Este projeto é de uso interno da Wdias Assessoria Rural e Engenharia.

---

Desenvolvido com ❤️ para facilitar a visualização e análise de dados geoespaciais.