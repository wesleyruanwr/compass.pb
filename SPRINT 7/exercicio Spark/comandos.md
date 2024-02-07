- pull da imagem

docker pull jupyter/all-spark-notebook


- criar um container a partir da imagem

docker run -p 8888:8888 jupyter/all-spark-notebook


- executar o container

docker exec -it "id do container" bash


- executar o pyspark

  pyspark


- criar um contador de palavras

from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col

spark = SparkSession.builder \
    .appName("Contagem de Palavras") \
    .getOrCreate()

df = spark.read.text("/home/jovyan/pasta/README.md")
- eu coloquei o arquivo README dentro de uma pasta no container
contador_palavras = df.select(explode(split(df.value, " ")).alias("word")) \
    .filter(col("word") != "") \
    .groupBy("word") \
    .count() \
    .orderBy("count", ascending=False)

contador_palavras.show()

spark.stop()
