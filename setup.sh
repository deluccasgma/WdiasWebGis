#!/usr/bin/env bash
# Instalar dependências do sistema para GDAL
mkdir -p $HOME/.apt/usr/lib
mkdir -p $HOME/.apt/usr/include

# Instalar GDAL via apt
apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libspatialindex-dev \
    libgeos-dev \
    libproj-dev

# Configurar variáveis de ambiente
export GDAL_DATA=/usr/share/gdal
export PROJ_LIB=/usr/share/proj