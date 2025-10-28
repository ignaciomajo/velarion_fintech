# Usa a imagem oficial do Apache Airflow (já vem com o Airflow instalado)
FROM apache/airflow:2.8.0-python3.10

# Troca para root só para criar diretórios e ajustar permissões
USER root

RUN mkdir -p /home/airflow/NoCountry/velarion_fintech/airflow-pipeline \
    && chown -R airflow:root /home/airflow/NoCountry \
    && chmod -R 777 /home/airflow/NoCountry

# Volta para o usuário padrão "airflow"
USER airflow

# Instala apenas pacotes extras, não o Airflow
RUN pip install --no-cache-dir psycopg2-binary pandas scikit-learn python-dotenv
