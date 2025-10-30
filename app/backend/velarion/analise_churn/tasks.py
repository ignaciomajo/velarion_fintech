from celery import shared_task
import requests
import psycopg2
from datetime import datetime

from django.conf import settings

db = settings.DATABASES['default']

DB_CONFIG = {
    "dbname": db['NAME'],
    "user": db['USER'],
    "password": db['PASSWORD'],
    "host": db['HOST'],
    "port": db['PORT']
}

API_URL = "http://127.0.0.1:8000/"

# Mapa entre nomes do banco e nomes esperados pelo modelo
FIELD_MAP = {
    "customerid": "CustomerId",
    "surname": "Surname",
    "creditscore": "CreditScore",
    "geography_germany": "Geography_Germany",
    "geography_spain": "Geography_Spain",
    "gender_male": "Gender_Male",
    "age": "Age",
    "tenure": "Tenure",
    "balance": "Balance",
    "numofproducts": "NumOfProducts",
    "hascrcard": "HasCrCard",
    "isactivemember": "IsActiveMember",
    "estimatedsalary": "EstimatedSalary",
    "avg_tx_amount": "avg_tx_amount",
    "std_tx_amount": "std_tx_amount",
    "days_since_last_tx": "days_since_last_tx",
    "tx_q1q2_rate_of_change": "tx_q1q2_rate_of_change",
    "tx_q2q3_rate_of_change": "tx_q2q3_rate_of_change",
    "avg_ss_duration": "avg_ss_duration",
    "std_ss_duration": "std_ss_duration",
    "days_since_last_ss": "days_since_last_ss",
    "ss_q1q2_rate_of_change": "ss_q1q2_rate_of_change",
    "ss_q2q3_rate_of_change": "ss_q2q3_rate_of_change",
    "failed_ratio_spike_q2": "failed_ratio_spike_q2",
    "failed_ratio_spike_q3": "failed_ratio_spike_q3",
    "failed_ratio_volatility": "failed_ratio_volatility",
}

def rename_fields(data):
    """Renomeia as chaves conforme o mapa FIELD_MAP"""
    return {FIELD_MAP.get(k, k): v for k, v in data.items()}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@shared_task(acks_late=True, max_retries=2)
def update_churn_probabilities():
    print("update")
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("TRUNCATE TABLE churn_predictions RESTART IDENTITY;")
        print("✅ churn_predictions truncada e IDs reiniciados")

        # Seleciona todos os clientes e suas features
        cur.execute("""
            SELECT *
            FROM public.client_feature;
        """)

        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        for row in rows:
            user_data = dict(zip(columns, row))

            user_id = user_data.pop("id")  # remove o id do payload
            payload = rename_fields(user_data)
            # Envia os dados para o endpoint de predição
            response = requests.post(API_URL+"api/predict/", json=payload)

            if response.status_code == 200:
                result = response.json()
                prob = float(result.get("probability", 0))
                riesgo = result.get("riesgo",0)
                modelo = "LightGBM"
                # Atualiza a tabela churn_predictions
                cur.execute("""
                    INSERT INTO churn_predictions (
                        cliente_id,
                        prob_churn,
                        modelo,
                        data_execucao,
                        riesgo
                    ) VALUES (%s, %s, %s, %s,%s)
                """, (user_id, prob, modelo, datetime.now(),riesgo))

                print(f"✅ Cliente {user_id} inserido -> prob={prob}")


            else:
                print(f"⚠️ Erro na API para cliente {user_id}: {response.status_code}")

        conn.commit()

    except Exception as e:
        print(f"❌ Erro ao atualizar probabilidades: {e}")

    finally:
        if conn:
            conn.close()
