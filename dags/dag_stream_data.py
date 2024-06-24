from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic
import json

from python.src.extraer_data_api import obtenerUsuarioAPI


def crearTopic(topic:str)->None:

	admin=AdminClient({"bootstrap.servers":"kafka:19092"})

	if topic not in admin.list_topics().topics:

		print(f"Creando topic {topic}...")

		objeto_topic=NewTopic(topic=topic, num_partitions=3, replication_factor=1)

		admin.create_topics([objeto_topic])

		crearTopic(topic)

	else:

		print(f"Topic {topic} creado")

def enviarData()->None:

	crearTopic("usuarios")

	producer=Producer({"bootstrap.servers":"kafka:19092"})

	mensaje=obtenerUsuarioAPI()

	producer.produce("usuarios", json.dumps(mensaje))

	producer.flush()
	
	print("Usuario enviado correctamente")



with DAG("dag_stream_data",
		start_date=datetime(2024,6,24),
		description="DAG para obtener data en stream de la API",
		schedule_interval="@daily",
		catchup=False) as dag:

	tarea_enviar_data=PythonOperator(task_id="enviar_data", python_callable=enviarData)


tarea_enviar_data