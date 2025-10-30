import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from io import StringIO
from pathlib import Path





# Carrega variáveis de ambiente
BASE_DIR = Path(__file__).resolve().parent
path_csv = (BASE_DIR / ".." / ".." / "src").resolve()
load_dotenv(os.path.join(BASE_DIR, "..", ".env"))

def load_data():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    table = os.getenv("POSTGRES_TABLE")
    csv_file = path_csv / "latest_dataset2.csv"

    print(f"🔄 Iniciando carregamento do arquivo {path_csv} para {table}")

    # Lê CSV
    df = pd.read_csv(csv_file)
 
 #   df = df.where(pd.notnull(df), None)

    # Trunca tabela
    with conn.cursor() as cur:
        cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE;")
        print(f"🧹 Tabela {table} truncada.")

    # Carrega via COPY (eficiente)
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    cols = ", ".join(df.columns)
    print(f"colunas {cols} ")
    with conn.cursor() as cur:
        cur.copy_expert(f"COPY {table} ({cols}) FROM STDIN WITH CSV", buffer)
        conn.commit()

    conn.close()
    print(f"✅ Inseridos {len(df)} registros em {table}.")


if __name__ == "__main__":
    load_data()
