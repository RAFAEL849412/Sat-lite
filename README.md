# Sat-lite

Sat-lite é uma ferramenta de automação desenvolvida para interagir com satélites via gRPC, coletando dados de status, histórico e alertas. O projeto também oferece integração com FTP e suporte a login automatizado no Google Drive.

## Visão Geral

Este projeto fornece uma maneira eficiente e automatizada de gerenciar a comunicação com satélites via gRPC. Além disso, ele oferece funcionalidades para realizar operações em servidores FTP e atualizar scripts no Google Drive com facilidade.

## Funcionalidades

- Comunicação com o terminal de usuário Starlink via gRPC.
- Coleta de dados de status, histórico e alertas.
- Suporte a FTP, incluindo upload de arquivos.
- Integração com o Google Drive para login e gerenciamento de arquivos.
- Suporte a fallback de WebDriver local e remoto para interação com páginas web.

## Requisitos

- Python 3.7 ou superior.
- Bibliotecas Python necessárias:
  - `grpcio`
  - `ftplib`
  - `selenium`
  - `google-auth`
  - `google-api-python-client`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/RAFAEL849412/Sat-lite.git
   cd Sat-lite
   ```

2. Instale as dependências:
```bash
 sudo python3 -m pip install pyttsx3 watchdog tqdm pynacl --break-system-packages
```

3. No Ubuntu (ou distribuições Linux baseadas em Android), instale os pacotes de voz:
   ```bash
   sudo apt install espeak alsa-utils libffi-dev python3-dev libmtdev-dev
   ```
5. Habilite SSL no seu projeto Python. Adicione suporte SSL para conexões seguras! Solicitações
```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365 -subj "/CN=localhost" > /dev/null 2>&1
```
6. Execute o projeto:
   ```bash
   python main.py
   ```

## Licença

Este projeto está licenciado sob a MIT License.

