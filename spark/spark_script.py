from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from pyspark.sql import functions as F
from typing import Optional
import sys

from config import JDBC_URL, PROPIEDADES, TABLA, SERVIDOR_KAFKA, TOPIC

def crearSesion()->Optional[SparkSession]:

	paquetes="org.postgresql:postgresql:42.2.23,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0"

	try:

		return SparkSession.builder\
						.appName("SparkStreaming")\
						.config("spark.jars.packages", paquetes)\
						.getOrCreate()

	except Exception:

		print("Error al crear la sesion de Spark")
		sys.exit()

def leerTabla(spark:SparkSession, tabla:str)->DataFrame:

	return spark.read.jdbc(url=JDBC_URL, table=tabla, properties=PROPIEDADES)

def escribirTabla(df:DataFrame, tabla:str, modo:str="overwrite")->None:

	df.write.mode(modo).jdbc(url=JDBC_URL, table=tabla, properties=PROPIEDADES)

def conectarStreamKafka(spark:SparkSession)->Optional[DataFrame]:

	try:

		return spark.readStream\
					.format("kafka")\
					.option("kafka.bootstrap.servers", SERVIDOR_KAFKA)\
					.option("subscribe", TOPIC)\
					.option("startingOffsets", "earliest")\
					.load()

	except Exception as e:

		print("Error al conectarse a Kafka: {e}")
		sys.exit()

def dataframe_seleccionado(df:DataFrame)->DataFrame:

	esquema=StructType([StructField("nombre", StringType(), False),
						StructField("apellido", StringType(), False),
						StructField("genero", StringType(), False),
						StructField("direccion", StringType(), False),
						StructField("codigo_postal", StringType(), False),
						StructField("correo", StringType(), False),
						StructField("usuario", StringType(), False),
						StructField("fecha_nacimiento", DateType(), False),
						StructField("fecha_registro", DateType(), False),
						StructField("telefono", StringType(), False),
						StructField("imagen", StringType(), False)])

	columnas=["data.nombre", "data.apellido", "data.genero", "data.direccion", "data.correo", "data.usuario",
				"data.fecha_nacimiento", "data.telefono", "data.imagen"]

	return df.selectExpr("CAST(value AS STRING)")\
				.select(F.from_json(F.col("value"), esquema).alias("data"))\
				.select(columnas)


if __name__ == "__main__":

	spark=crearSesion()

	df=conectarStreamKafka(spark)

	df_seleccionado=dataframe_seleccionado(df)

	print("La sesion en streaming se esta iniciando...")

	df_seleccionado.writeStream\
					.outputMode("append")\
					.foreachBatch(lambda df, id_batch: escribirTabla(df, "usuarios", "append"))\
					.option("checkpointLocation", "/opt/spark/nacho/scripts/checkpoint")\
					.start()\
					.awaitTermination()