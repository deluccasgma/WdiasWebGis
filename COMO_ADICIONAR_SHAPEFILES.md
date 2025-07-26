# 📁 Como Adicionar Shapefiles ao WebGIS

## 🎯 Pré-requisitos

Um shapefile completo deve conter **pelo menos** estes arquivos:
- `nome.shp` - Geometrias (obrigatório)
- `nome.dbf` - Atributos (obrigatório) 
- `nome.shx` - Índice espacial (obrigatório)
- `nome.prj` - Sistema de coordenadas (recomendado)

## 📋 Passo a Passo

### 1. Preparar os Arquivos
```bash
# Exemplo de arquivos necessários:
meu_shapefile.shp    # Geometrias
meu_shapefile.dbf    # Tabela de atributos
meu_shapefile.shx    # Índice
meu_shapefile.prj    # Projeção (opcional)
meu_shapefile.cpg    # Codificação (opcional)
```

### 2. Copiar para o Diretório
```bash
# Copie todos os arquivos para o diretório do WebGIS
cp meu_shapefile.* /caminho/para/webgis/
```

### 3. Verificar Estrutura
```bash
# Liste os arquivos para confirmar
ls -la *.shp *.dbf *.shx
```

### 4. Executar o WebGIS
```bash
# Execute a aplicação
./run_webgis.sh
```

## 🗂️ Formatos Aceitos

### Geometrias Suportadas
- ✅ **Pontos** (Point)
- ✅ **Linhas** (LineString)
- ✅ **Polígonos** (Polygon)
- ✅ **MultiPolígonos** (MultiPolygon)
- ✅ **MultiPontos** (MultiPoint)
- ✅ **MultiLinhas** (MultiLineString)

### Sistemas de Coordenadas
- ✅ **Geográficos**: WGS84, SIRGAS2000, SAD69
- ✅ **Projetados**: UTM, Albers, Lambert
- ⚡ **Conversão Automática**: Para WGS84 na visualização

## 📊 Atributos Recomendados

### Para Propriedades Rurais
```
id          - Identificador único
nome        - Nome da propriedade
area        - Área em hectares
proprietario - Nome do proprietário
municipio   - Município
estado      - Estado
uso_solo    - Tipo de uso do solo
```

### Para Limites Municipais
```
codigo_ibge - Código IBGE
nome        - Nome do município
estado      - Estado
populacao   - População
area        - Área em km²
```

## 🔧 Ferramentas para Criar Shapefiles

### Software GIS
- **QGIS** (gratuito) - [qgis.org](https://qgis.org)
- **ArcGIS** (pago)
- **Global Mapper** (pago)

### Conversão Online
- **MyGeodata** - [mygeodata.cloud](https://mygeodata.cloud)
- **GDAL/OGR** - Linha de comando

### Exemplo com QGIS
1. Abrir QGIS
2. Criar nova camada vetorial
3. Definir geometria e atributos
4. Desenhar features
5. Salvar como Shapefile

## ⚠️ Problemas Comuns

### Erro: "Arquivo não encontrado"
**Causa**: Faltam arquivos obrigatórios
**Solução**: Verifique se `.shp`, `.dbf` e `.shx` existem

### Erro: "Geometria inválida"
**Causa**: Polígonos auto-intersectantes
**Solução**: Use "Fix geometries" no QGIS

### Erro: "Codificação incorreta"
**Causa**: Caracteres especiais não reconhecidos
**Solução**: Salve com codificação UTF-8

### Mapa não centraliza
**Causa**: Sistema de coordenadas incorreto
**Solução**: Adicione arquivo `.prj` correto

## 📈 Otimização de Performance

### Para Shapefiles Grandes
```bash
# Simplificar geometrias (QGIS)
Vector > Geometry Tools > Simplify

# Reduzir precisão de coordenadas
# Use 6 casas decimais para graus (±11cm)
```

### Limites Recomendados
- **Features**: Máximo 10.000
- **Vértices por polígono**: Máximo 1.000
- **Tamanho do arquivo**: Máximo 50MB

## 🧪 Teste Seus Dados

### Verificação Rápida
```python
import geopandas as gpd

# Carregar shapefile
gdf = gpd.read_file('seu_arquivo.shp')

# Informações básicas
print(f"Features: {len(gdf)}")
print(f"CRS: {gdf.crs}")
print(f"Colunas: {list(gdf.columns)}")
print(f"Geometrias válidas: {gdf.geometry.is_valid.sum()}")
```

## 📞 Suporte

Se encontrar problemas:
1. Verifique este guia
2. Teste com QGIS primeiro
3. Entre em contato: gilmar@wdias.eng.br

---

**💡 Dica**: Sempre mantenha backup dos shapefiles originais!