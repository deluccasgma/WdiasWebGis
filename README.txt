# WebGIS com Python, Streamlit e Folium

## Como rodar o projeto

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

2. Coloque os arquivos do seu Shapefile ( .shp, .shx, .dbf, .prj … ) em qualquer pasta do repositório (por exemplo `Shapefile/`). O aplicativo localiza o primeiro .shp automaticamente, mesmo se estiver em sub-pastas.

3. Execute o aplicativo:
   ```
   streamlit run app.py
   ```

4. O mapa será aberto no navegador. Você pode alternar entre 3 mapas de fundo e exibir/ocultar a camada vetorial.

- O zoom inicial foca automaticamente na área do vetor carregado. 