#parte 1

from pyspark.sql import SparkSession

from pyspark import SparkContext, SQLContext

spark = SparkSession \
    .builder \
    .master("local[*]")\
    .appName("Exercicio Intro") \
    .getOrCreate()

df = spark.read.csv("C:/Users/Wesley Ruan/compass.pb/SPRINT 8/Exercícios Apache Spark/nomes_aleatorios.txt", header=False, inferSchema=True)

df.show(5)

#parte 2

df = df.withColumnRenamed("_c0", "Nomes")

df.printSchema()

#df.show(10)

#parte 3
from pyspark.sql import functions as F

df = df.withColumn("Escolaridade",
            F.when(F.rand() < 0.33, "Fundamental")
            .when(F.rand() < 0.66, "Medio")
            .otherwise("Superior"))

df.show(10)

#parte 4
from pyspark.sql.functions import when, rand

df = df.withColumn("Pais",
    when(rand() < 1/13, "Brasil").\
    when(rand() < 2/13, "Argentina").\
    when(rand() < 3/13, "Colombia").\
    when(rand() < 4/13, "Chile").\
    when(rand() < 5/13, "Peru").\
    when(rand() < 6/13, "Venezuela").\
    when(rand() < 7/13, "Equador").\
    when(rand() < 8/13, "Bolivia").\
    when(rand() < 9/13, "Paraguai").\
    when(rand() < 10/13, "Uruguai").\
    when(rand() < 11/13, "Guiana").\
    when(rand() < 12/13, "Suriname").\
    otherwise("Guiana Francesa")
)

df.show(10)

#parte 5

from pyspark.sql.functions import rand

df = df.withColumn("AnoNascimento", (rand(seed=42) * (2010 - 1945 + 1) + 1945).cast("int"))

df.show(10)

#parte 6

from pyspark.sql.functions import col

df = df.filter(col("AnoNascimento") > 2000)

df.select("Nomes").show(10, truncate=False)

df.show(10)

#parte 7

df.createOrReplaceTempView("pessoas")

df_select_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento > 2000")

df_select_sql.select("Nomes").show(10, truncate=False)

#parte 8

num_millennials = df.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()

print("Número de pessoas da geração Millennials:", num_millennials)

#parte 9

num_millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]

print("Número de pessoas da geração Millennials:", num_millennials_sql)

#parte 10

from pyspark.sql import functions as F

df.createOrReplaceTempView("pessoas")

consulta_sql = """
    SELECT Pais, 
           CASE 
               WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
               WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
               WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
               WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
               ELSE 'Outra'
           END AS Geracao,
           COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, 
             CASE 
                 WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                 WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
                 WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
                 WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
                 ELSE 'Outra'
             END
"""

# Executando a consulta SQL
df_resultado = spark.sql(consulta_sql)

df_resultado = df_resultado.orderBy("Pais", "Geracao", "Quantidade")

df_resultado.show()
