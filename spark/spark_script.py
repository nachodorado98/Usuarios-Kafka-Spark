from pyspark.sql import SparkSession

spark=SparkSession.builder\
				.appName("SparkStreaming")\
				.getOrCreate()

data=[(1, "Nacho"), (2, "Amanda")]

columnas=["Id", "Nombre"]

df=spark.createDataFrame(data, columnas)

df.show()

spark.stop()