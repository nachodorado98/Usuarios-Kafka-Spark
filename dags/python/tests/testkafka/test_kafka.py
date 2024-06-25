import pytest

from src.kafka.topic_kafka import crearTopic

@pytest.mark.parametrize(["topic"],
	[("hola",), ("topic1",), ("topic_prueba",)]
)
def test_topic_no_existe(admin, topic):

	assert topic not in admin.list_topics().topics

@pytest.mark.parametrize(["topic"],
	[("hola",), ("topic1",), ("topic_prueba",)]
)
def test_topic_existe(admin, topic):

	assert topic not in admin.list_topics().topics

	crearTopic(topic)

	assert topic in admin.list_topics().topics

	admin.delete_topics(topics=[topic])