from pyspark.sql import SparkSession

from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()

df = spark.read.csv("C:/Users/Wesley Ruan/compass.pb/SPRINT 8/Exercícios Apache Spark/nomes_aleatorios.txt", header=False, inferSchema=True)

df.show(5)