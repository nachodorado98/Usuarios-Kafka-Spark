from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

from config import JDBC_URL, PROPIEDADES, TABLA

def crearSesion()->SparkSession:

	try:

		return SparkSession.builder\
						.appName("SparkStreaming")\
						.config("spark.jars.packages", "org.postgresql:postgresql:42.2.23")\
						.getOrCreate()

	except Exception:

		print("Error al crear la sesion")

def crearDataframe(spark:SparkSession)->DataFrame:

	data=[(1, "Nacho"),(2, "Amanda")]

	esquema=StructType([StructField("Id", IntegerType(), False), StructField("Nombre", StringType(), False)])

	return spark.createDataFrame(data, schema=esquema)

def leerTabla(tabla:str)->DataFrame:

	return spark.read.jdbc(url=JDBC_URL, table=tabla, properties=PROPIEDADES)

def escribirTabla(df:DataFrame, tabla:str, modo:str="overwrite")->None:

	df.write.mode(modo).jdbc(url=JDBC_URL, table=tabla, properties=PROPIEDADES)

try:

	spark=crearSesion()

	df=crearDataframe(spark)

	escribirTabla(df, TABLA)

	df_tabla=leerTabla(TABLA)

	df_tabla.show()

except Exception:

	print("Error en la ejecucion")

finally:

	spark.stop()