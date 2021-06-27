# Constroi uma nova imagem
# docker build -t my-python-app .

# Executa o aplicativo
# docker run -it --rm --name my-running-app my-python-app

# Imagem oficial
FROM python:3

# Busca atualizações no repositório
RUN apt-get update

# Adiciona os arquivos no projeto
ADD . /app

# Diretório default do projeto
WORKDIR /app

# Executa o arquivo requirements para instalar as suas bibliotecas 
RUN pip install --no-cache-dir -r requirements.txt
