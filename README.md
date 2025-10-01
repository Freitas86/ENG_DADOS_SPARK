# ENG_DADOS_SPARK

Este repositório contém um ambiente de estudo e prática com **Python**, **Poetry** e **JupyterLab** no **WSL (Windows Subsystem for Linux)**.  
Abaixo seguem os comandos necessários para configurar e executar o projeto.

---

## 🔧 Instalação do Python no WSL

```bash
sudo apt update
sudo apt upgrade
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
python3.10 --version
```

---

## ▶️ Comandos para rodar o projeto no WSL

```bash
# Clonar o repositório
git clone https://github.com/Freitas86/ENG_DADOS_SPARK.git
cd ENG_DADOS_SPARK

# Instalar dependências básicas
sudo apt install python3-pip
sudo apt install python3-poetry

# Ativar ambiente virtual com Poetry
poetry shell

# Instalar Jupyter
sudo apt install jupyter-core
pip install jupyterlab

# Acessar os notebooks
cd notebooks/
jupyter lab
```

Depois de rodar o último comando, abra no navegador:  
👉 [http://localhost:8888/lab](http://localhost:8888/lab)

---

## 📌 Observações

- Certifique-se de que o **WSL** esteja atualizado.
- Caso o `poetry shell` não funcione, verifique se o Poetry foi instalado corretamente (`poetry --version`).
- Os notebooks estarão disponíveis na pasta `notebooks/`.

---
