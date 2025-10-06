# **Fintech - Customer Churn**

<img width="720" height="640" alt="nano-banana-2025-10-06T15-03-15" src="https://github.com/user-attachments/assets/9622b396-bf2e-4f82-a06b-64d332cdf90b" />

---

## Índice 📋

1. Descripción del proyecto
2. Acceso al proyecto
3. Etapas del proyecto
4. Data Catalog (Catálogo de datos)
5. Resultados y conclusiones
6. Tecnologías utilizadas
7. Agradecimientos
8. Desarrolladores del proyecto

---


## 1. Descripción del proyecto 📚

Este proyecto de Data Science se centra en la predicción de abandono de clientes (churn) para el sector Fintech. El objetivo principal es desarrollar un modelo predictivo que identifique a los clientes con alta probabilidad de dejar de usar los servicios, permitiendo así a los equipos de negocio implementar estrategias de retención proactivas y personalizadas.

Para lograrlo, se utilizan datos de transacciones, interacciones con la aplicación y otros factores relevantes. El resultado final es un modelo de Machine Learning y un panel de control interactivo (dashboard) que ofrece una visión clara de los segmentos de riesgo y recomendaciones accionables para mejorar las tasas de retención. Este enfoque no solo busca mitigar la pérdida de ingresos, sino también optimizar los costos de retención al dirigir las campañas de forma más efectiva.


## 2. Acceso al proyecto 📂

Para obtener el proyecto tienes dos opciones:

1. Clonar el repositorio utilizando la línea de comandos. Solo debes dirigirte al directorio donde deseas clonar el mismo e ingresar el comando:
   `git clone https://github.com/ignaciomajo/******`

2. O puedes descargarlo directamente desde el repositorio en GitHub en el siguiente enlace:
   [https://github.com/ignaciomajo/******](https://github.com/ignaciomajo/******)

   Esto te llevará a la siguiente pantalla, donde deberás seguir los siguientes pasos:

<img width="1831" height="685" alt="image" src="https://github.com/user-attachments/assets/74d11ea0-0f9b-43f9-8b61-70d26483b30f" />

   
Esto descargará un archivo comprimido `.zip`, que podrás alojar en el directorio que desees.


## 3. Etapas del proyecto 📝

<br><br><br><br><br>


## 4. Data Catalog (Catálogo de datos)
El dataset resultante para el entrenamiento de los modelos fue confexionado a partir de distintas fuentes:

* <a href=https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers>Dataset Churn</a>
* <a href="https://www.kaggle.com/datasets/ealaxi/paysim1>https://www.kaggle.com/datasets/ealaxi/paysim1">Dataset PaySim</a>

### Features: Perfil del Cliente

| Feature               | Tipo                | Descripción                                                    | 
|-----------------------|---------------------|----------------------------------------------------------------| 
| `CustomerId`          | Categórica Nominal  | Identificador único del cliente                                |
| `CreditScore`         | Numérica Discreta   | Score crediticio del cliente                                   |
| `Geography`           | Categórica Discreta | País de residencia del cliente                                 |
| `Gender`              | Categórica Binaria  | Género del cliente                                             |
| `Age`                 | Numérica Discreta   | Edad del cliente                                               |
| `Tenure`              | Numérica Discreta   | Antigüedad del cliente                                         |
| `Balance`             | Numérica Continua   | Balance del cliente                                            |
| `HasCrCard`           | Categórica Binaria  | Condición del cliente si posee tarjeta de crédito o no         |
| `IsActiveMember`      | Categórica Binaria  | Condición del cliente, registrado como cliente activo o pasivo |
| `EstimatedSalary`     | Numérica Continua   | Salario estimado del cliente                                   |


  avg_amount_30d = client_tx[client_tx['date'] >= d30_back]['amount'].mean()
  if pd.isna(avg_amount_30d): 
      avg_amount_30d = 0
  ratio_recent_vs_historical_transactions_amount = safe_ratio(avg_amount_30d, avg_txs_amount)
  risk_factor = vulnerability_score * avg_inflation
  inf_pressure = (1 - ratio_recent_vs_historical_transactions_amount) * risk_factor

### Features: Transacciones

| Feature                       | Tipo               | Descripción                                                                                                              | 
|-------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| `days_since_last_tx`          | Numérica Discreta  | Días desde la última transacción                                                                                         |
| `txs_avg_amount`              | Numérica Continua  | Monto promedio de transacción                                                                                            |
| `amount_std`                  | Numérica Continua  | Desviación estandar de los montos de las transacciones del cliente                                                       |
| `avg_cashout_amount`          | Numérica Continua  | Monto promedio de retiro de dinero                                                                                       |
| `ratio_recent_vs_past_txs`    | Numérica Continua  | Ratio que considera la actividad en los últimos 30 días en comparación con los 60 días anteriores a estos 30.            |
| `ratio_recent_vs_past_amount` | Numérica Continua  | Ratio que considera el monto transaccionado en los últimos 30 días en comparación con los 60 días anteriores a estos 30. |
| `ratio_cashouts`              | Numérica Continua  | Ratio de cantidad de retiros de dinero en relación a la cantidad total de transacciones                                  |
| `ratio_transfers`             | Numérica Continua  | Ratio de cantidad de transferencias de dinero en relación a la cantidad total de transacciones                           |
| `inflation_pressure`          | Numérica Continua  | Ratio que mide vulnerabilidad del cliente frente a la inflación de su país de residencia                                 |


* `ratio_recent_vs_past_txs`: 
  - Logaritmo (Transacciones en los ultimos 30 días / Transacciones desde `CUTOFF_DATE - 30 días` hasta `CUTOFF_DATE - 90 días` )
* `ratio_recent_vs_past_amount`:
  - Logaritmo (Monto total en los ultimos 30 días / Monto total desde `CUTOFF_DATE - 30 días` hasta `CUTOFF_DATE - 90 días` )
* `ratio_cashouts`:
  - Logaritmo (Cantidad de transacciones CASH_OUT / Cantidad total de transacciones)
* `ratio_transfers`: 
  - Logaritmo (Cantidad de transacciones TRANSFER / Cantidad total de transacciones

* `inflation_pressure`:
  
    ```
    vulnerability_score = [1, 2, 3]
    
    # Inflación promedio para el período observado
    avg_inflation = inflation_periodo['inflation_rate'].mean()
    
    avg_amount_30d = client[client['date'] >= d30_back]['amount'].mean()
    if pd.isna(avg_amount_30d): 
        avg_amount_30d = 0
    ratio_recent_vs_historical_transactions_amount = safe_ratio(avg_amount_30d, avg_txs_amount)
    risk_factor = vulnerability_score * avg_inflation
    inf_pressure = (1 - ratio_recent_vs_historical_transactions_amount) * risk_factor
    ```

    
### Features: Interacción con la Aplicación del Banco

| Feature                       | Tipo               | Descripción                                                                                                                                           | 
|-------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|`days_since_last_ss`           | Numérica Discreta  | Días desde la último login                                                                                                                            |
|`total_ss_past30d`             | Numérica Discreta  | Cantidad de logins en los últimos 30 días                                                                                                             |
|`total_ss_past90d`             | Numérica Discreta  | Cantidad de logins en los últimos 90 días                                                                                                             |
|`avg_ss_per_wk`                | Numérica Continua  | Cantidad de logins promedio por semana                                                                                                                |
|`total_ss_duration_min`        | Numérica Continua  | Cantidad total en minutos de la duración de los logins del cliente (tiempo total utilizando la aplicación)                                            |
|`avg_ss_duration_min`          | Numérica Continua  | Duración promedio en minutos de logins del cliente                                                                                                    |
|`std_ss_duration_min`          | Numérica Continua  | Desviación estandar de la duración en minutos del login del cliente                                                                                   |
|`avg_cashout_amount`           | Numérica Continua  | Monto promedio de retiro de dinero                                                                                                                    |
|`ratio_ss_time_recent_vs_past` | Numérica Continua  | Ratio que considera el tiempo de utilización de la aplicación del banco en los últimos 30 días en comparación con los 60 días anteriores a estos 30.  |
|`ratio_events_sessios`         | Numérica Continua  | Ratio que considera el uso de funcionalidades de la aplicación: [`used_transfer`, `used_payment`, `used_invest`], en relación a la cantidad de logins.|
|`ratio_failed_ss`              | Numérica Continua  | Ratio de cantidad de intentos de login fallidos en relación a la cantidad total de logins                                                             |
|`total_opened_push`            | Numérica Discreta  | Cantidad total de notificaciones abiertas dentro de la aplicación.                                                                                    |

* `ratio_ss_time_recent_vs_past`: 
  - Logaritmo (Duración total en minutos en los ultimos 30 días / Duración total en minutos desde `CUTOFF_DATE - 30 días` hasta `CUTOFF_DATE - 90 días` )
* `ratio_events_sessios`: 
  - Logaritmo (Suma total de funcionalidades utilizadas / Cantidad total de logins desde)
* `ratio_failed_ss`: 
  - Logaritmo (Cantidad de `failed_login` / Cantidad total de logins)

## 5. Resultados y conclusiones

<br><br><br><br><br>


## 6. Tecnologías utilizadas 🛠️

* ``
* `Git and GitHub`
* ``
* ``
* ``


## 7. Agradecimientos 🤝

<br><br><br><br><br>


## 8. Desarrolladores del proyecto 👷
