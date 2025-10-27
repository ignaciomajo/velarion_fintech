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
    --password admin

# Iniciar serviços (em background)
echo "🚀 Iniciando webserver e scheduler..."
airflow webserver -p 8080 &
airflow scheduler &

echo "✅ Airflow iniciado com sucesso em http://localhost:8080"
