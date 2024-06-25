import os
import sys
sys.path.append(os.path.abspath(".."))

import pytest

from confluent_kafka.admin import AdminClient

from src.kafka.configkafka import SERVIDOR

@pytest.fixture()
def admin():

	return AdminClient({"bootstrap.servers":SERVIDOR})