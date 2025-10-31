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

1. Clonar el repositorio utilizando la línea de comandos. Solo debes dirigirte al directorio donde deseas clonar el mismo e ingresar el comando:<br><br>
   `git clone https://github.com/ignaciomajo/velarion_fintech`

2. O puedes descargarlo directamente desde el repositorio en GitHub en el siguiente enlace:<br>

   [https://github.com/ignaciomajo/velarion_fintech](https://github.com/ignaciomajo/velarion_fintech)

   Esto te llevará a la siguiente pantalla, donde deberás seguir los siguientes pasos:

<img width="1831" height="685" alt="image" src="https://github.com/user-attachments/assets/74d11ea0-0f9b-43f9-8b61-70d26483b30f" />

   
Esto descargará un archivo comprimido `.zip`, que podrás alojar en el directorio que desees.


## 3. Etapas del proyecto 📝

1. [Consolidación Datasets Iniciales](https://github.com/ignaciomajo/velarion_fintech/blob/main/datasets_consolidation_Velarion.ipynb)
2. [Análisis Exploratorio de Datos](https://github.com/ignaciomajo/velarion_fintech/blob/main/EDA_Velarion.ipynb)
3. [Modelado de datos](https://github.com/ignaciomajo/velarion_fintech/blob/main/Modeling_Velarion.ipynb)
4. [Datos artificiales de prueba](https://github.com/ignaciomajo/velarion_fintech/blob/main/datos_artificiales_prueba_Velarion.ipynb)
5. [Deslpiegue API](https://velarion-fintech.onrender.com/api/docs/#/predict/)
6. [Dashboard de control](https://github.com/ignaciomajo/velarion_fintech/blob/main/dashboard/velarion_dashboard2.pbix)
<br>

## 4. Data Catalog (Catálogo de datos)

### [ml_dataset.csv](https://github.com/ignaciomajo/velarion_fintech/blob/main/src/ml_dataset.csv)

El dataset resultante para el entrenamiento de los modelos fue confexionado a partir de distintas fuentes:

* <a href=https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers>Dataset Churn</a>
* <a href="https://www.kaggle.com/datasets/ealaxi/paysim1>https://www.kaggle.com/datasets/ealaxi/paysim1">Dataset PaySim</a>
* [app_sessions.parquet](https://github.com/ignaciomajo/velarion_fintech/blob/main/datasets_consolidation_Velarion.ipynb) - Sección: **App Interaction** (generado con ayuda de IA, el código se encuentra dentro del script)
* [IPCAs](https://github.com/ignaciomajo/velarion_fintech/blob/main/datasets_consolidation_Velarion.ipynb) Sección: **Factor Externo**(toma los registros de HICP — IPCA en español — de [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/tec00118/default/table?lang=en) que contiene registros hasta 2024, y luego estimación generada con IA para los valores de 2024-08 hasta 2025-09)

#### Target

| Feature               | Tipo                | Descripción                                                    | 
|-----------------------|---------------------|----------------------------------------------------------------| 
| `Exited`              | Categórica Binaria  | Condición de abandono dentro de la ventana de tiempo observada |


#### **Ventanas Temporales**

Para llevar los datos de tiempo a un formato tabular se consideró una ventana de análisis de 365 días.

| VENTANA       | Período          | Comienzo          | Final            | Descripción                                           |
|---------------|------------------|-------------------|------------------|-------------------------------------------------------|
| WINDOW_1      | Q1               | 2024-09-30        | 2025-01-02       | Primer trimestre para observación del comportamiento  | 
| WINDOW_2      | Q2               | 2025-01-03        | 2025-04-02       | Segundo trimestre para observación del comportamiento |
| WINDOW_3      | Q3               | 2025-04-03        | 2025-07-01       | Tercer trimestre para observación del comportamiento  |
| CUTOFF_DATE   | Q4               | 2025-07-02        | 2025-09-30       | Ventana de Churn                                      |


#### **Features: Perfil del Cliente**

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


#### **Features: Transacciones**

| Feature                       | Tipo               | Descripción                                                                                                                   | 
|-------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `days_since_last_tx`          | Numérica Discreta  | Días desde la última transacción                                                                                              |
| `avg_tx_amount`               | Numérica Continua  | Monto promedio de transacción                                                                                                 |
| `std_tx_amount`               | Numérica Continua  | Desviación estandar de los montos de las transacciones del cliente                                                            |
| `tx_q1q2_rate_of_change`      | Numérica Continua  | Ratio que considera la cantidad de transacciones en el primer trimestre (Q1) en comparación con el segundo trimestre(Q2)      |
| `tx_q1q2_rate_of_change`      | Numérica Continua  | Ratio que considera la cantidad de transacciones en el segundo trimestre (Q2) en comparación con el tercer trimestre (Q3)     |

**Nota**: `client` representa una fila

> **`tx_q1q2_rate_of_change`**
```
client['tx_q1q2_rate_of_change'] = (client['total_tx_q2'] - client['total_tx_q1']) / client['total_tx_q1']
```

> **`tx_q2q3_rate_of_change`**
```
client['tx_q2q3_rate_of_change'] = (client['total_tx_q3'] - client['total_tx_q2']) / client['total_tx_q2']
```

#### Features: Interacción con la Aplicación de la empresa

| Feature                        | Tipo               | Descripción                                                                                                                     | 
|--------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `days_since_last_ss`           | Numérica Discreta  | Días desde la último login                                                                                                      |
| `avg_ss_duration_min`          | Numérica Continua  | Duración promedio en minutos de logins del cliente                                                                              |
| `std_ss_duration_min`          | Numérica Continua  | Desviación estandar de la duración en minutos del login del cliente                                                             |
| `ss_q1q2_rate_of_change`       | Numérica Continua  | Ratio que considera la cantidad de sesiones (logins) en el primer trimestre (Q1) en comparación con el segundo trimestre(Q2)    |
| `ss_q1q2_rate_of_change`       | Numérica Continua  | Ratio que considera la cantidad de sesiones (logins) en el segundo trimestre (Q2) en comparación con el tercer trimestre (Q3)   |
| `failed_ratio_spike_q2`        | Numérica Continua  | Diferencia entre el ratio del primer trimestre (Q1) y el segundo trimestre (Q2)                                                 |
| `failed_ratio_spike_q3`        | Numérica Continua  | Diferencia entre el ratio del primer trimestre (Q2) y el segundo trimestre (Q3)                                                 |
| `failed_ratio_volatility`      | Numérica Continua  | Desviación estandar calculada a partir del ratio de fallos de los 3 tirmestres [Q1, Q2, Q3]                                     |      


**Nota**: `client` representa una fila

> **`ss_q1q2_rate_of_change`**
```
client['ss_q1q2_rate_of_change'] = (client['total_ss_q2'] - client['total_ss_q1']) / client['total_ss_q1']
```

> **`ss_q2q3_rate_of_change`**
```
client['ss_q2q3_rate_of_change'] = (client['total_tx_q3'] - client['total_tx_q2']) / client['total_tx_q2']
```

> **`failed_ratio_spike_q2`**
```
client['failed_ratio_spike_q2'] = (client['total_failed_ss_q2'] / client['total_ss_q2']) - (client['total_failed_ss_q1'] / client['total_ss_q1'])
```

> **`failed_ratio_spike_q3`**
```
client['failed_ratio_spike_q3'] = (client['total_failed_ss_q3'] / client['total_ss_q3']) - (client['total_failed_ss_q2'] / client['total_ss_q2'])
```

> **`failed_ratio_volatility`** 
```
client['failed_ratio_volatility'] = [(client['total_failed_ss_q1'] / client['total_ss_q1']), (client['total_failed_ss_q2'] / client['total_ss_q2']), (client['total_failed_ss_q3'] / client['total_ss_q3'])].std()
```


## 5. Resultados y conclusiones

A partir del análisis realizado, uno de los puntos más criticos determinados fue que la mayor tasa de evasión corresponde a los clientes de más valor de la empresa. Esto representa un espacio crítico de observación y desarrollo de estrategias de retención.

<img width="1770" height="868" alt="exit_rate_cluster_label" src="https://github.com/user-attachments/assets/a714e496-3450-41b5-a37b-18bc75fe609a" />


A su vez, se vió que el rango etario de mayor riesgo se encuentra entre los 38 y 51 años, estos son clientes de mediana edad. 
Para este grupo, pensar en invertir a menudo no es una opción, sino una necesidad más estructurada.

* **Prioridades Clave**: Suelen estar en sus años de mayores ingresos. Sus preocupaciones principales son la jubilación (que ven más cercana), la educación de los hijos y el pago de hipotecas.
* **Comportamiento**: La inversión es más planificada. Tienen, en promedio, más capital para invertir y tienden a usar instrumentos más tradicionales como fondos de inversión y planes de pensiones. Suelen ser un poco más conservadores porque tienen más que perder y menos tiempo para recuperarse de grandes caídas.
* **El "Pensamiento"**: Su pensamiento sobre la inversión es más estratégico, enfocado en la preservación del capital y el crecimiento constante a largo plazo.

Por lo que si se combinan clientes "VIP" y en este rango de edad, indica que la empresa está perdiendo clientes no solo valiosos, sino que deberían ser potenciales inversores.

Las variables más relevantes para la predicción fueron (de mayor a menor influencia):

> `Age`: Mayor predictor. La contribución a las probabilidades relativas de abandono aumentan drásticamente cuando la edad del cliente se encuentra por encima de la media.

> `NumOfProducts`: Si bien valores elevados para este feautre parece actuar como protector contra el abandono, también se observa que valores altos pero no máximos contribuyen al abandono, esto podría indicar insatisfacción con algún producto en particular.

> `ss_q2q3_rate_of_change`: Fuerte predictor de Churn. Si este ratio tiene un valor negativo (estandarizado) entre -1.5 y -0.5, las probabilidades relativas de abandono aumentan considerablemente -> **-0.5 UMBRAL CRÍTICO DE MONITOREO**

> `IsActiveMember`: Gran protector contra el abandono, será esencial generar estrategias que mantengan al cliente en un estado activo.

> `days_since_last_tx`: Factor de alto riesgo, a medida que pasan los días sin que el cliente realize transacciones, más aumentan las probabilidades relativas de abandono.

> `Gender_Male`: El hecho de ser mujer (`Gender_Male = 0`) actúa como potenciador en las probabilidades relativas de Churn. Este es un punto crítico a investigar dado que puede haber sesgos de género en productos, ofertas y/o condiciones -> **IMPORTANTE REVISAR POLÍTICAS DE EMPRESA**.

> `Geography_Germany`: Ser alemán aumenta las probabilidades relativas de abandono. Será necesario investigar las razones por las cuales los clientes de este país son más propensos a abandonar la empresa.

> `days_since_last_ss`: Al igual que días desde la última transacción, mientras más días pasa un cliente sin conectarse a la aplicación de la empresa, más aumenta el riesgo de abandono.

> `Balance`: CRÍTICO -> Tener un alto balance contribuye a las probabilidades relativas de abandono, esto refleja que los clientes que deciden dejar la empresa son de alto valor. Resulta de suma importancia investigar este fenómeno en profundidad.


## 6. Tecnologías utilizadas 🛠️

* `Jupyter Notebook`
* `Git and GitHub`
* `Power BI`
* `FastAPI`


## 7. Agradecimientos 🤝

Agradecer a No Country, la empresa encargada de la simulación laboral, quien presentó el contexto del proyecto y la plataforma para conectar a los integrantes y promover el trabajo colaborativo

<img width="252" height="98" alt="image" src="https://github.com/user-attachments/assets/81f9b116-b58a-4a6f-a8e6-0df46bda5456" />



## 8. Desarrolladores del proyecto 👷

* **Samantha Estudillo**
  - Rol: BI Analyst / Data Analyst
* **Patricio Diaz**
  - Rol: Data Analyst / Data Scientist
* **Carlos Silva**
  - Rol: ML Engineer
* **Ignacio Majo**
  - Rol: Data Engineer / Data Scientist
    
