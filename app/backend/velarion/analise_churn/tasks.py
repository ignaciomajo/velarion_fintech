from celery import shared_task
import requests
import psycopg2
from datetime import datetime

DB_CONFIG = {
    "dbname": "db_velarion",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": 5432
}

API_URL = "http://127.0.0.1:8000/api/predict/"

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@shared_task
def update_churn_probabilities():
    print("update")
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Seleciona todos os clientes e suas features
        cur.execute("""
            SELECT id, "CreditScore", "Age", "Tenure", "Balance", "NumOfProducts",
                   "HasCrCard", "IsActiveMember", "EstimatedSalary", days_since_last_tx,
                   txs_avg_amount, amount_std, avg_cashout_amount, ratio_recent_vs_past_txs,
                   ratio_recent_vs_past_amount, ratio_cashouts, ratio_transfers,
                   inflation_pressure, days_since_last_ss, total_ss_past30d, total_ss_past90d,
                   avg_ss_per_wk, avg_ss_duration_min, std_ss_duration_min,
                   ratio_ss_time_recent_vs_past, ratio_events_sessios, ratio_failed_ss,
                   total_opened_push
            FROM public.client_feature;
        """)

        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        for row in rows:
            user_data = dict(zip(columns, row))
            user_id = user_data.pop("id")  # remove o id do payload

            # Envia os dados para o endpoint de predição
            response = requests.post(API_URL, json=user_data)

            if response.status_code == 200:
                result = response.json()
                prob = float(result.get("probability", 0))
                modelo = "RNN"
                # Atualiza a tabela churn_predictions
                cur.execute("""
                    INSERT INTO churn_predictions (
                        cliente_id,
                        prob_churn,
                        modelo,
                        data_execucao
                    ) VALUES (%s, %s, %s, %s)
                """, (user_id, prob, modelo, datetime.now()))

                print(f"✅ Cliente {user_id} inserido -> prob={prob:.3f}")


            else:
                print(f"⚠️ Erro na API para cliente {user_id}: {response.status_code}")

        conn.commit()

    except Exception as e:
        print(f"❌ Erro ao atualizar probabilidades: {e}")

    finally:
        if conn:
            conn.close()
