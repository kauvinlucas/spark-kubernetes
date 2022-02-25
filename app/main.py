# Basado en el ejemplo del libro "Spark - The definite Guide":
# https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/Production_Applications-Chapter_16_Spark_Applications.py

# in Python
from __future__ import print_function
import time
if __name__ == '__main__':
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .master("local") \
        .appName("Word Count") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    print("***********Sesion Created***********")
    print(spark.range(5000).where("id > 500").selectExpr("sum(id)").collect())
    print("***********Waiting 5***********")
    time.sleep(5)
    print("***********Finished***********")