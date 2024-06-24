from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from python.src.extraer_data_api import obtenerUsuarioAPI

def obtenerData()->None:

	print(obtenerUsuarioAPI())

with DAG("dag_prueba",
		start_date=datetime(2024,6,24),
		description="DAG para obtener data en stream de la API",
		schedule_interval="@daily",
		catchup=False) as dag:

	tarea_obtener_data=PythonOperator(task_id="obtener_data", python_callable=obtenerData)


tarea_obtener_data