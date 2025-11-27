# Downloader GUI (Python + ttkbootstrap)

Uma aplicação simples e eficiente para baixar arquivos usando **wget**,
**curl** ou **requests**, com interface gráfica moderna em
**ttkbootstrap**.\
Ideal para testes de download, ambientes sem navegador e verificações de
velocidade em redes.

------------------------------------------------------------------------

## 📌 Funcionalidades

-   ✔ Interface moderna com ttkbootstrap\
-   ✔ **Ferramenta padrão: wget**\
-   ✔ Barra de progresso\
-   ✔ Velocidade em tempo real\
-   ✔ ETA (tempo estimado)\
-   ✔ Histórico dos últimos downloads\
-   ✔ Escolha da pasta de destino\
-   ✔ Totalmente offline (exceto o download em si)\
-   ✔ Funciona no Windows/Linux/macOS\
-   ✔ Útil para testar links, espelhos e servidores

------------------------------------------------------------------------

## 📦 Requisitos

### Python

Requer **Python 3.8 ou superior**.

### Dependências

Instale com:

``` bash
pip install ttkbootstrap requests
```

### Ferramentas externas (opcionais)

#### Windows

-   **wget**: https://eternallybored.org/misc/wget/\
-   **curl**: já vem no Windows 10/11

#### Linux / macOS

-   **wget**: geralmente já vem instalado\
-   **curl**: já acompanha o sistema

------------------------------------------------------------------------

## ▶ Como executar

``` bash
python main.py
```

------------------------------------------------------------------------

## 📝 Como usar

1.  Cole o link do arquivo no campo de **URL**.\
2.  Selecione a ferramenta (**wget**, **curl** ou **requests**).\
3.  Clique em **Baixar**.\
4.  Acompanhe a barra de progresso, velocidade e ETA.\
5.  Verifique o arquivo na pasta selecionada.

------------------------------------------------------------------------

## 🌐 Exemplos de URLs para teste

### 🔹 Arquivos grandes (100 MB -- 10 GB)

| Tamanho | URL |
|---------|-----|
| 100 MB  | https://speed.hetzner.de/100MB.bin |
| 1 GB    | https://speed.hetzner.de/1GB.bin |
| 10 GB   | https://speed.hetzner.de/10GB.bin |
| 512 MB  | http://ipv4.download.thinkbroadband.com/512MB.zip |

------------------------------------------------------------------------

### 🔹 Arquivos médios (1 -- 50 MB)

| Tamanho | URL |
|--------:|-----|
| 10 MB   | http://speedtest.tele2.net/10MB.zip |
| 20 MB   | http://speedtest.tele2.net/20MB.zip |
| 50 MB   | http://speedtest.tele2.net/50MB.zip |

------------------------------------------------------------------------

### 🔹 Arquivos pequenos (até 1 MB)

  -------------------------------------------------------------------
| Tamanho     | URL |
|-------------|-----|
| 100 KB      | http://speedtest.tele2.net/100KB.zip |
| 1 MB        | http://speedtest.tele2.net/1MB.zip |
| Logo Google | https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png |

------------------------------------------------------------

### 🔹 ISOs para testar velocidade (1 GB -- 5 GB)

  --------------------------------------------------------------------
| Sistema            | URL |
|--------------------|-----|
| Ubuntu 24.04       | https://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso |
| Debian 12          | https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso |
| Fedora Workstation | https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso |

  --------------------------------------------------------------------


### 🔹 Arquivos RAW do GitHub

    https://raw.githubusercontent.com/vim/vim/master/runtime/scripts.vim
    https://raw.githubusercontent.com/python/cpython/main/README.rst
    https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
    https://raw.githubusercontent.com/torvalds/linux/master/README

------------------------------------------------------------------------

## 📚 Observações importantes

-   *wget* é a opção mais estável para downloads grandes.\
-   A barra de progresso detalhada funciona melhor usando *requests*.\
-   Caso não selecione uma pasta, o arquivo será salvo no diretório do
    programa.\
-   Informações como velocidade e ETA dependem do servidor.

------------------------------------------------------------------------

## 📦 Criar executável (Windows)

Use PyInstaller:

``` bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

O executável será gerado em:

    dist/main.exe

------------------------------------------------------------------------