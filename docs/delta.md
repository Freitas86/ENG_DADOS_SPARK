# Delta Lake

## Criando uma tabela Delta

```sql
CREATE TABLE delta_trips
USING delta
LOCATION 'file:///tmp/datalake/delta_trips'
AS SELECT * FROM trips_raw LIMIT 0;
```

Ou via API PySpark:

```python
df.write.format("delta").mode("overwrite").save("/tmp/datalake/delta_trips")
spark.sql("CREATE TABLE IF NOT EXISTS default.delta_trips USING DELTA LOCATION '/tmp/datalake/delta_trips'")
```

## Exemplos de operações

### INSERT
```python
new_df.write.format("delta").mode("append").save("/tmp/datalake/delta_trips")
```

### UPDATE
```python
from delta.tables import DeltaTable
dt = DeltaTable.forPath(spark, "/tmp/datalake/delta_trips")
dt.update("trip_id = 'SOME_ID'", {"fare_amount": "fare_amount * 1.10"})
```

### DELETE
```python
dt.delete("passenger_count = 0")
```

### MERGE
```python
dt.alias("t").merge(
    source=updates_df.alias("s"),
    condition="t.trip_id = s.trip_id",
    whenMatchedUpdate={"fare_amount": "s.fare_amount"},
    whenNotMatchedInsertAll=True
).execute()
```