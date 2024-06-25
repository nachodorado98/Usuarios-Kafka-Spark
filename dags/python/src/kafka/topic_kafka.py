from confluent_kafka.admin import AdminClient, NewTopic

from .configkafka import SERVIDOR

def crearTopic(topic:str)->None:

	admin=AdminClient({"bootstrap.servers":SERVIDOR})

	if topic not in admin.list_topics().topics:

		print(f"Creando topic {topic}...")

		objeto_topic=NewTopic(topic=topic, num_partitions=3, replication_factor=1)

		admin.create_topics([objeto_topic])

		crearTopic(topic)

	else:

		print(f"Topic {topic} creado")