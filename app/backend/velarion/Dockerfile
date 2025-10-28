# Dockerfile para Django Velarion
FROM python:3.10-slim

# Evita prompts de tzdata
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Copia requirements.txt
COPY requirements.txt .

# Instala dependências
RUN apt-get update && apt-get install -y libgomp1 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia todo o backend
COPY . .

# Expõe porta padrão do Django
EXPOSE 8000

# Comando padrão para rodar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
