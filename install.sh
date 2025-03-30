#!/bin/bash

# Mensagem de boas-vindas
echo "Olá! Verificando requisitos para instalação..."

# Verifica se o script está sendo executado como root
if [[ $EUID -ne 0 ]]; then
  echo "Erro: Este script deve ser executado como root ou com sudo."
  exit 1
fi

# Nome do pacote a ser instalado
PACOTE="curl"

# Verifica se o pacote já está instalado
if command -v $PACOTE &> /dev/null; then
  echo "O pacote $PACOTE já está instalado."
else
  echo "Instalando o pacote $PACOTE..."
  apt update && apt install -y $PACOTE
  if [[ $? -eq 0 ]]; then
    echo "O pacote $PACOTE foi instalado com sucesso."
  else
    echo "Erro ao instalar o pacote $PACOTE."
    exit 1
  fi
fi

echo "Verificação concluída. O cliente está pronto para uso!"
