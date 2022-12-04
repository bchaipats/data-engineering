from pyspark.sql import SparkSession

log_file = "/home/bcp/workspace/data-engineering/README.md"
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
log_data = spark.read.text(log_file).cache()

num_As = log_data.filter(log_data.value.contains('a')).count()
num_Bs = log_data.filter(log_data.value.contains('b')).count()

print(f"Lines with a: {num_As}, lines with b: {num_Bs}")

spark.stop()
