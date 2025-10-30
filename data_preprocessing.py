
import os
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import pickle

# ====================================
#               PATHS
# ====================================

extension = '.parquet'


# Obtiene el path actual
PROJECT_PATH = Path(__file__).resolve().parent


src = Path('src')
DATA_PATH = PROJECT_PATH / src

tx = Path('tx')
TX_DATA_PATH = DATA_PATH / tx

app = Path('app')
APP_DATA_PATH = DATA_PATH/ app

champion = Path('champion')
CHAMPION_PATH = PROJECT_PATH / champion

img = Path('img')
IMG_PATH = PROJECT_PATH / img

models = Path('models')
MODELS_PATH = PROJECT_PATH / models

reports = Path('reports')
REPORTS_PATH = PROJECT_PATH / reports


# ====================================
#         EXTRACCIÓN DE DATOS
# ====================================


df_tx = []
df_ss = []


rutas_files = [TX_DATA_PATH, APP_DATA_PATH]


archivos_encontrados = 0

for ruta in rutas_files:
    for carpeta_actual, lista_carpetas, lista_archivos in os.walk(ruta):
        for archivo in lista_archivos:
            if archivo.endswith(extension):
                if archivo.startswith('tx'):
                    file=pd.read_parquet(os.path.join(carpeta_actual, archivo))
                    df_tx.append(file)
                    archivos_encontrados += 1
                elif archivo.startswith('ss'):
                    file=pd.read_parquet(os.path.join(carpeta_actual, archivo))
                    df_ss.append(file)
                    archivos_encontrados += 1
                else:
                    pass
            else:
                pass

if archivos_encontrados > 0:
    print(f'\nTotal de archivos encontrados: {archivos_encontrados}')
else:
    print(f'No se encontraron archivos con extension {extension}')



# ====================================
#         VENTANAS DE TIEMPO
# ====================================

TODAY = datetime.today()

WINDOW_Q3_START = TODAY - pd.Timedelta(days=90)
WINDOW_Q2_END = TODAY - pd.Timedelta(days=91)
WINDOW_Q2_START = TODAY - pd.Timedelta(days=180)
WINDOW_Q1_END = TODAY - pd.Timedelta(days=181)
WINDOW_Q1_START = TODAY - pd.Timedelta(days=270)

df_tx = pd.concat(df_tx, ignore_index=True)
df_ss = pd.concat(df_ss, ignore_index=True)

df_tx = df_tx[(df_tx['date'] >= WINDOW_Q1_START) & (df_tx['date'] < TODAY)]
df_ss = df_ss[(df_ss['date'] >= WINDOW_Q1_START) & (df_ss['date'] < TODAY)]

df_tx.sort_values(by='date', inplace=True)
df_ss.sort_values(by='date', inplace=True)

df_clients = pd.read_parquet(DATA_PATH/'clients_no_churners.parquet')

clients_uniques = df_clients['CustomerId'].unique()



# ======================================
#  Feature Engineering - Transacciones
# ======================================

CUTOFF_DATE = TODAY
# Crea un DataFrame para los features
features_tx = df_tx.groupby('CustomerId').agg(
    avg_tx_amount=('amount', 'mean'),
    std_tx_amount=('amount', 'std'),
    total_tx=('amount', 'count'),
    last_tx_date=('date', 'max')
).reset_index()

features_tx['days_since_last_tx'] = (CUTOFF_DATE - features_tx['last_tx_date']).dt.days


txs_q1 = df_tx[(df_tx['date'] >= WINDOW_Q1_START) & (df_tx['date'] < WINDOW_Q1_END)]
txs_q2 = df_tx[(df_tx['date'] >= WINDOW_Q2_START) & (df_tx['date'] < WINDOW_Q2_END)]
txs_q3 = df_tx[(df_tx['date'] >= WINDOW_Q3_START) & (df_tx['date'] < CUTOFF_DATE)]

total_tx_q1 = txs_q1.groupby('CustomerId').size().reset_index(name='total_tx_q1')
total_tx_q2 = txs_q2.groupby('CustomerId').size().reset_index(name='total_tx_q2')
total_tx_q3 = txs_q3.groupby('CustomerId').size().reset_index(name='total_tx_q3')

features_tx = features_tx.merge(total_tx_q1, on='CustomerId')
features_tx = features_tx.merge(total_tx_q2, on='CustomerId')
features_tx = features_tx.merge(total_tx_q3, on='CustomerId')

features_tx['tx_q1q2_rate_of_change'] = (features_tx['total_tx_q2'] - features_tx['total_tx_q1']) / features_tx['total_tx_q1']
features_tx['tx_q2q3_rate_of_change'] = (features_tx['total_tx_q3'] - features_tx['total_tx_q2']) / features_tx['total_tx_q2']


tx_uniques = df_tx['CustomerId'].unique()
df_clients_filtered = df_clients[df_clients['CustomerId'].isin(tx_uniques)]


consolidated_ds = df_clients_filtered.merge(features_tx, on='CustomerId')




# ========================================
#  Feature Engineering - App Interactions
# ========================================

# Crea un DataFrame para los features
features_ss = df_ss.groupby('CustomerId').agg(
    avg_ss_duration=('duration_min', 'mean'),
    std_ss_duration=('duration_min', 'std'),
    total_ss=('duration_min', 'count'),
    last_ss_date=('date', 'max')
).reset_index()


features_ss['days_since_last_ss'] = (CUTOFF_DATE - features_ss['last_ss_date']).dt.days



ss_q1 = df_ss[(df_ss['date'] >= WINDOW_Q1_START) & (df_ss['date'] < WINDOW_Q1_END)]
ss_q2 = df_ss[(df_ss['date'] >= WINDOW_Q2_START) & (df_ss['date'] < WINDOW_Q2_END)]
ss_q3 = df_ss[(df_ss['date'] >= WINDOW_Q3_START) & (df_ss['date'] < CUTOFF_DATE)]

total_ss_q1 = ss_q1.groupby('CustomerId').size().reset_index(name='total_ss_q1')
total_ss_q2 = ss_q2.groupby('CustomerId').size().reset_index(name='total_ss_q2')
total_ss_q3 = ss_q3.groupby('CustomerId').size().reset_index(name='total_ss_q3')

total_failed_ss_q1 = ss_q1.groupby('CustomerId')['failed_login'].sum().reset_index(name='total_failed_ss_q1')
total_failed_ss_q2 = ss_q2.groupby('CustomerId')['failed_login'].sum().reset_index(name='total_failed_ss_q2')
total_failed_ss_q3 = ss_q3.groupby('CustomerId')['failed_login'].sum().reset_index(name='total_failed_ss_q3')

features_ss = features_ss.merge(total_ss_q1, on='CustomerId')
features_ss = features_ss.merge(total_ss_q2, on='CustomerId')
features_ss = features_ss.merge(total_ss_q3, on='CustomerId')
features_ss = features_ss.merge(total_failed_ss_q1, on='CustomerId')
features_ss = features_ss.merge(total_failed_ss_q2, on='CustomerId')
features_ss = features_ss.merge(total_failed_ss_q3, on='CustomerId')


def calculate_session_change_rate(row, previous_q, followed_q):
    freq_past = row[previous_q]
    freq_last = row[followed_q]
    
    if freq_past == 0:
        if freq_last > 0:
            return 1.0 
        else:
            return 0.0
    else:
        return (freq_last - freq_past) / freq_past
    

features_ss['ss_q1q2_rate_of_change'] = features_ss.apply(
                                        lambda row: calculate_session_change_rate(row, 'total_ss_q1', 'total_ss_q2'), 
                                        axis=1)

features_ss['ss_q2q3_rate_of_change'] = features_ss.apply(
                                            lambda row: calculate_session_change_rate(row, 'total_ss_q2', 'total_ss_q3'), 
                                            axis=1)

def safe_division(numerator, denominator):
    return numerator / denominator if denominator > 0 else 0.0

features_ss['failed_ratio_q1'] = features_ss.apply(
    lambda row: safe_division(row['total_failed_ss_q1'], row['total_ss_q1']), axis=1
)
features_ss['failed_ratio_q2'] = features_ss.apply(
    lambda row: safe_division(row['total_failed_ss_q2'], row['total_ss_q2']), axis=1
)
features_ss['failed_ratio_q3'] = features_ss.apply(
    lambda row: safe_division(row['total_failed_ss_q3'], row['total_ss_q3']), axis=1
)


# Diferencia entre el ratio del último período y el anterior
features_ss['failed_ratio_spike_q2'] = features_ss['failed_ratio_q2'] - features_ss['failed_ratio_q1']
features_ss['failed_ratio_spike_q3'] = features_ss['failed_ratio_q3'] - features_ss['failed_ratio_q2']


# Selecciona las columnas de ratio
ratio_cols = ['failed_ratio_q1', 'failed_ratio_q2', 'failed_ratio_q3']

# Calcula la desviación estándar para cada fila (axis=1)
features_ss['failed_ratio_volatility'] = features_ss[ratio_cols].std(axis=1)    


ss_uniques = features_ss['CustomerId'].unique()
consolidated_ds = consolidated_ds[consolidated_ds['CustomerId'].isin(ss_uniques)]

consolidated_ds = consolidated_ds.merge(features_ss, on='CustomerId')

# consolidated_ds.drop(['RowNumber', 'Surname', 'vulnerability_tier', 'vulnerability_score',
#                       'total_tx_q1', 'total_tx_q2', 'total_tx_q3','total_ss_q1', 'total_ss_q2', 'total_ss_q3', 'failed_ratio_q1',
#                       'total_failed_ss_q1', 'total_failed_ss_q2', 'total_failed_ss_q3',
#                       'failed_ratio_q2', 'failed_ratio_q3', 'last_tx_date', 'last_ss_date', 'total_tx','total_ss'],
#                      axis=1,
#                      inplace=True)

consolidated_ds.drop(['RowNumber', 'vulnerability_tier', 'vulnerability_score',
                      'total_tx_q1', 'total_tx_q2', 'total_tx_q3','total_ss_q1', 'total_ss_q2', 'total_ss_q3', 'failed_ratio_q1',
                      'total_failed_ss_q1', 'total_failed_ss_q2', 'total_failed_ss_q3',
                      'failed_ratio_q2', 'failed_ratio_q3', 'last_tx_date', 'last_ss_date', 'total_tx','total_ss'],
                     axis=1,
                     inplace=True)


# ====================================
#               OBJETOS
# ====================================


with open(CHAMPION_PATH / 'one_hot_encoder.pkl', 'rb') as f:
    one_hot_encoder = pickle.load(f)
    
with open(CHAMPION_PATH / 'scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
with open(CHAMPION_PATH / 'categoricas.pkl', 'rb') as f:
    categoricas = pickle.load(f)
    
with open(CHAMPION_PATH / 'numericas.pkl', 'rb') as f:
    numericas = pickle.load(f)
    
with open(CHAMPION_PATH / 'col_order.pkl', 'rb') as f:
    col_order = pickle.load(f)

latest_cids = consolidated_ds['CustomerId'].values.copy()

with open(CHAMPION_PATH / 'latest_cids.pkl', 'wb') as f:
    pickle.dump(latest_cids, f)


#consolidated_ds.drop('CustomerId', axis=1, inplace=True)
consolidated_ds.to_csv(DATA_PATH/ 'latest_dataset2.csv', index=False)
# ====================================
#    ENCODING VARIABLES CATEGÓRICAS
# ====================================

ds_encoded = one_hot_encoder.transform(consolidated_ds)

columnas = one_hot_encoder.get_feature_names_out()
columnas_encoded = []
for columna in columnas:
    columna = columna.split('__')[1]
    columnas_encoded.append(columna)

df_encoded = pd.DataFrame(ds_encoded, 
                          columns=columnas_encoded, 
                          index=consolidated_ds.index)

# ====================================
#    ESCALADO VARIABLES NUMÉRICAS
# ====================================

df_encoded[numericas] = scaler.transform(df_encoded[numericas])

final_dataset = df_encoded[col_order]


# ==============================
#     GUARDADO DATASET FINAL
# ==============================

final_dataset.to_csv(DATA_PATH/ 'latest_dataset.csv', index=False)