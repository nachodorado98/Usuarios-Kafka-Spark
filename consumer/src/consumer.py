from confluent_kafka import Consumer, KafkaError
from confluent_kafka.admin import AdminClient
import time

from .configkafka import TOPIC, SERVIDOR

def ejecutarConsumer()->None:

	admin=AdminClient({"bootstrap.servers":SERVIDOR})

	if TOPIC not in admin.list_topics().topics:

		print(f"Topic {TOPIC} no existente")

		time.sleep(5)

		ejecutarConsumer()

	consumer=Consumer({"bootstrap.servers": SERVIDOR, "group.id":"grupo1"})

	consumer.subscribe([TOPIC])

	print("Escuchando...")

	while True:

		mensaje=consumer.poll(timeout=100)

		if mensaje is None:

			continue

		if mensaje.error():

			if mensaje.error().code()==KafkaError._PARTITION_EOF:

				continue

			else:

				print(mensaje.error())

				break

		print(mensaje.value().decode("utf-8"))