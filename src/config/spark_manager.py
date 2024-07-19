import os
os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk-11"
os.environ["SPARK_HOME"] = "C:\spark-3.5.1-bin-hadoop3"
# import findspark # type: ignore
# findspark.init()
from pyspark.sql import SparkSession
spark_session = (SparkSession.builder.master('local[*]').appName('finance-complaint').getOrCreate())
                #  .config("spark.executor.instances", '1')
                #  .config("spark.executor.memory", '6g')
                #  .config("spark.driver.memory", '6g')
                #  .config("spark.executor.memoryOverhead", '8g')
                #   )