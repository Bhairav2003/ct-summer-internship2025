from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from datetime import datetime

jdbc_hostname = "DESKTOP-MKADE9M"        
jdbc_port = 1433
jdbc_database = "CDC_Project_DB"
jdbc_username = "bhairav"
jdbc_password = "Bh@irav2025#Sql"

jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:{jdbc_port};databaseName={jdbc_database};encrypt=false"

connection_properties = {
    "user": jdbc_username,
    "password": jdbc_password,
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


adls_base_path = "abfss://your-container@storageproject159.dfs.core.windows.net/cdc-output"  


def get_last_timestamp(table_name):
    try:
        df = spark.read.format("delta").load(f"{adls_base_path}/{table_name}")
        return df.agg({"last_updated": "max"}).collect()[0][0]
    except:
        return None

def read_table_incrementally(table_name):
    last_ts = get_last_timestamp(table_name)
    query = f"(SELECT * FROM {table_name} WHERE last_updated > '{last_ts}') AS t" if last_ts else table_name
    return spark.read.jdbc(url=jdbc_url, table=query, properties=connection_properties)

def process_and_write(table_name):
    df = read_table_incrementally(table_name)
    df = df.withColumn("load_date", lit(datetime.now()))
    df.write.format("delta").mode("append").save(f"{adls_base_path}/{table_name}")
    print(f"✅ {table_name} written to Delta Lake.")

tables = ["Customer", "Product", "OrderTbl", "Inventory"]

for tbl in tables:
    process_and_write(tbl)
