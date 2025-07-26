# 🗺️ WebGIS - Wdias Assessoria Rural e Engenharia

Um sistema WebGIS moderno desenvolvido com Streamlit e Folium para visualização e análise de dados geoespaciais.

## ✨ Funcionalidades

- **🔐 Sistema de Login**: Controle de acesso por usuário
- **🗺️ Múltiplas Camadas de Base**: OpenStreetMap, Stamen Terrain, CartoDB, Satélite
- **📁 Visualização de Shapefiles**: Suporte completo a arquivos .shp
- **🎨 Personalização de Estilo**: Cores, opacidade e espessura de bordas
- **💬 Popups Informativos**: Exibição dos atributos do shapefile
- **📍 Centroide**: Opção para mostrar o centroide do polígono
- **🖥️ Plugins Úteis**: Tela cheia, minimapa, controle de camadas
- **📊 Estatísticas**: Informações sobre geometrias, área e sistema de coordenadas

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório**:
```bash
git clone https://github.com/seu-usuario/WdiasWebGis.git
cd WdiasWebGis
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

3. **Execute o aplicativo**:
```bash
streamlit run app.py
```

4. **Acesse no navegador**:
```
http://localhost:8501
```

## 👥 Usuários de Acesso

| Usuário | Senha | Tipo |
|---------|-------|------|
| admin | senhaadm | Administrador |
| deluccasgma@gmail.com | Lg1401@@ | Administrador |
| usuario1 | senha1 | Usuário |
| usuario2 | senha2 | Usuário |
| gilmar@wdias.eng.br | 123456 | Usuário |

## 📁 Estrutura do Projeto

```
WdiasWebGis/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
├── packages.txt          # Dependências do sistema (se necessário)
├── ÁREA_DO_IMOVEL.shp    # Shapefile principal
├── ÁREA_DO_IMOVEL.dbf    # Arquivo de atributos
├── ÁREA_DO_IMOVEL.prj    # Sistema de coordenadas
├── ÁREA_DO_IMOVEL.shx    # Índice espacial
└── ÁREA_DO_IMOVEL.cpg    # Codificação de caracteres
```

## 🛠️ Como Usar

### 1. Login
- Acesse a aplicação no navegador
- Use um dos usuários listados acima para fazer login

### 2. Visualização do Mapa
- O shapefile será carregado automaticamente
- Use o controle de camadas para alternar entre diferentes mapas de base
- Clique nos polígonos para ver os atributos

### 3. Configurações
- **Sidebar**: Configure opções de visualização
- **Estilo**: Personalize cores e opacidade do shapefile
- **Plugins**: Use tela cheia e minimapa para melhor navegação

### 4. Informações
- **Estatísticas**: Veja métricas do shapefile na parte superior
- **Dados**: Acesse a tabela de atributos na seção "Informações Adicionais"

## 🔧 Personalização

### Adicionar Novos Shapefiles
1. Coloque os arquivos .shp na raiz do projeto
2. O sistema detectará automaticamente novos shapefiles
3. Use o seletor na sidebar para alternar entre eles

### Modificar Usuários
Edite a seção `usuarios` no arquivo `app.py`:
```python
usuarios = {
    "novo_usuario": "nova_senha",
    # ... outros usuários
}
```

### Alterar Estilo Padrão
Modifique as variáveis de estilo na seção correspondente do código:
```python
fill_color = "#3388ff"      # Cor de preenchimento
fill_opacity = 0.3          # Opacidade
border_color = "#000000"    # Cor da borda
border_width = 2            # Espessura da borda
```

## 🌐 Deploy

### Streamlit Cloud
1. Faça push do código para o GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. Configure o arquivo principal como `app.py`

### Heroku
1. Crie um arquivo `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Deploy usando Heroku CLI ou GitHub integration

### Docker
1. Crie um `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🐛 Solução de Problemas

### Erro ao carregar shapefile
- Verifique se todos os arquivos do shapefile estão presentes (.shp, .dbf, .prj, .shx)
- Confirme se o sistema de coordenadas é suportado

### Problemas de dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Erro de permissão
```bash
chmod +x app.py
```

## 📞 Suporte

Para suporte técnico, entre em contato:
- **Email**: gilmar@wdias.eng.br
- **Empresa**: Wdias Assessoria Rural e Engenharia

## 📄 Licença

Este projeto é desenvolvido pela Wdias Assessoria Rural e Engenharia.

---

**Desenvolvido com ❤️ usando Streamlit + Folium + GeoPandas**