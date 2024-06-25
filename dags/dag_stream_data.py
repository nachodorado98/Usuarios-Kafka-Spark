from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from confluent_kafka import Producer
import json
import time

from python.src.extraer_data_api import obtenerUsuarioAPI
from python.src.kafka.topic_kafka import crearTopic
from python.src.kafka.configkafka import SERVIDOR, TOPIC


def enviarDataStream()->None:

	producer=Producer({"bootstrap.servers":SERVIDOR})

	tiempo_actual=time.time()

	while True:

		if time.time()>tiempo_actual+60:

			break

		try:

			mensaje=obtenerUsuarioAPI()

			producer.produce(TOPIC, json.dumps(mensaje).encode("utf-8"))

			producer.flush()

			print("Usuario enviado correctamente")

		except Exception:

			print("Error al enviar el usuario")



with DAG("dag_stream_data",
		start_date=datetime(2024,6,24),
		description="DAG para obtener data en stream de la API",
		schedule_interval="@daily",
		catchup=False) as dag:

	tarea_crear_topic=PythonOperator(task_id="crear_topic", python_callable=lambda : crearTopic(TOPIC))

	tarea_enviar_data_stream=PythonOperator(task_id="enviar_data_stream", python_callable=enviarDataStream)


tarea_crear_topic >> tarea_enviar_data_stream