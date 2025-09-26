from pyspark.sql import SparkSession

def build_spark(app_name="pyspark-datalakes"):
    packages = [
        "io.delta:delta-core_2.12:2.2.0",
        "org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0"
    ]
    packages_str = ",".join(packages)

    builder = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.jars.packages", packages_str)
        .config("spark.sql.extensions",
                "io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.sql.catalog.local_iceberg", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.local_iceberg.type", "hadoop")
        .config("spark.sql.catalog.local_iceberg.warehouse", "file:///tmp/iceberg_warehouse")
    )
    return builder.getOrCreate()
