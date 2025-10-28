#!/usr/bin/env bash
set -e


# Carregar variáveis de ambiente
echo "📦 Carregando variáveis de ambiente..."
export $(grep -v '^#' .env | xargs)

# Criar diretórios necessários
mkdir -p $AIRFLOW_HOME/dags $AIRFLOW_HOME/logs $AIRFLOW_HOME/plugins

# Inicializar banco de dados do Airflow
echo "🧩 Inicializando banco de dados do Airflow..."
airflow db init

# Criar usuário admin (se não existir)
echo "👤 Criando usuário admin..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin || true  # evita erro se já existir

# Iniciar scheduler em background
airflow scheduler &

# Iniciar webserver em foreground (mantém o container ativo)
echo "🚀 Iniciando webserver..."
exec airflow webserver -p 8080
