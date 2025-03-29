#!/bin/bash

# Lista de URLs para baixar
URLS=(
    "https://example.com/arquivo1.zip"
    "https://example.com/arquivo2.zip"
    "https://example.com/arquivo3.zip"
)

# Diretório para salvar os arquivos
DESTINO="$HOME/Sat-lite"

# Criar diretório se não existir
mkdir -p "$DESTINO"

# Baixar os arquivos
for URL in "${URLS[@]}"; do
    echo "Baixando $URL para $DESTINO..."
    wget -P "$DESTINO" "$URL"
done

echo "Downloads concluídos na pasta $DESTINO!"