# 🗺️ WebGIS - Wdias Assessoria Rural e Engenharia

Sistema de Informações Geográficas baseado na web para visualização e análise de dados espaciais.

## 🚀 Funcionalidades

### 📊 Visualização de Dados
- **Suporte a Shapefiles**: Carregamento automático de arquivos `.shp`
- **Múltiplas Camadas**: OpenStreetMap, Satélite, Terreno, CartoDB
- **Popups Informativos**: Detalhes completos de cada feature
- **Colorização por Atributos**: Visualização temática baseada em campos numéricos

### 🛠️ Ferramentas Interativas
- **Medição**: Distâncias e áreas diretamente no mapa
- **Localização GPS**: Encontre sua posição atual
- **Tela Cheia**: Visualização otimizada
- **Zoom e Pan**: Navegação fluida no mapa

### 📈 Análise de Dados
- **Estatísticas**: Contagem de features e área total
- **Tabela de Atributos**: Visualização dos dados tabulares
- **Informações de Clique**: Coordenadas da posição selecionada
- **Cálculo de Áreas**: Automático para polígonos

### 🔐 Sistema de Autenticação
- **Login Seguro**: Controle de acesso por usuário
- **Níveis de Permissão**: Usuários comuns e administradores
- **Sessão Persistente**: Mantém login durante uso

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Sistema operacional: Linux, macOS ou Windows
- Navegador web moderno

## 🛠️ Instalação

### Método 1: Script Automático (Recomendado)
```bash
# Tornar o script executável
chmod +x run_webgis.sh

# Executar o WebGIS
./run_webgis.sh
```

### Método 2: Manual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run app.py
```

## 📁 Estrutura de Arquivos

```
webgis/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências Python
├── run_webgis.sh         # Script de execução
├── README.md             # Este arquivo
├── .streamlit/
│   └── config.toml       # Configurações do Streamlit
├── venv/                 # Ambiente virtual (criado automaticamente)
└── *.shp, *.dbf, *.shx, *.prj  # Arquivos shapefile
```

## 🗂️ Formatos Suportados

### Shapefiles
- **Obrigatórios**: `.shp`, `.dbf`, `.shx`
- **Opcionais**: `.prj` (sistema de coordenadas), `.cpg` (codificação)
- **Geometrias**: Pontos, Linhas, Polígonos, MultiPolígonos

### Sistemas de Coordenadas
- **Entrada**: Qualquer sistema suportado pelo GDAL
- **Visualização**: Automática conversão para WGS84 (EPSG:4326)

## 👤 Usuários Padrão

| Usuário | Senha | Tipo |
|---------|-------|------|
| admin | senhaadm | Administrador |
| deluccasgma@gmail.com | Lg1401@@ | Administrador |
| gilmar@wdias.eng.br | 123456 | Usuário |
| usuario1 | senha1 | Usuário |
| usuario2 | senha2 | Usuário |

## 🎨 Interface

### 🏠 Tela Principal
- **Header**: Logo e título da aplicação
- **Sidebar**: Controles e configurações
- **Mapa**: Visualização principal dos dados
- **Painel Lateral**: Estatísticas e informações

### ⚙️ Controles Disponíveis
- **Seleção de Shapefile**: Dropdown com arquivos disponíveis
- **Opções de Visualização**: Checkbox para mostrar/ocultar camadas
- **Controle de Opacidade**: Slider para transparência
- **Colorização**: Seleção de campo para colorir features

## 📊 Dados do Shapefile Exemplo

O shapefile `ÁREA_DO_IMOVEL.shp` contém:
- **2 features** (polígonos)
- **Sistema de coordenadas**: EPSG:4674 (SIRGAS 2000)
- **Campos disponíveis**:
  - `recibo`: Código identificador
  - `modfiscais`: Módulos fiscais
  - `tema`: Tema da propriedade
  - `area`: Área em hectares
  - `municipio`: Município
  - `estado`: Estado

## 🔧 Configurações Técnicas

### Dependências Principais
- **Streamlit**: Interface web
- **Folium**: Mapas interativos
- **GeoPandas**: Manipulação de dados geoespaciais
- **Shapely**: Operações geométricas
- **PyProj**: Transformações de coordenadas

### Configurações do Servidor
- **Porta padrão**: 8501
- **Modo desenvolvimento**: Desabilitado
- **CORS**: Configurado para uso local

## 📱 Compatibilidade

### Navegadores Testados
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Dispositivos
- 💻 Desktop/Laptop
- 📱 Tablet (parcialmente)
- 📱 Mobile (limitado)

## 🚨 Solução de Problemas

### Erro: "Nenhum shapefile encontrado"
- Verifique se os arquivos `.shp`, `.dbf` e `.shx` estão no diretório
- Certifique-se de que os arquivos têm os mesmos nomes base

### Erro de dependências
```bash
# Reinstalar dependências
pip install --upgrade -r requirements.txt
```

### Problemas de performance
- Reduza a complexidade dos polígonos
- Use shapefiles com menos features para teste
- Verifique a memória RAM disponível

## 🤝 Contribuições

Para contribuir com o projeto:
1. Faça fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📞 Suporte

**Wdias Assessoria Rural e Engenharia**
- 📧 Email: gilmar@wdias.eng.br
- 🌐 Web: [wdias.eng.br](http://wdias.eng.br)

## 📄 Licença

Este projeto é desenvolvido para uso interno da Wdias Assessoria Rural e Engenharia.

---

**Desenvolvido com ❤️ para análise geoespacial eficiente**