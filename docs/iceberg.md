# Apache Iceberg

## Criando uma tabela Iceberg

```sql
CREATE TABLE local_iceberg.default.iceberg_trips (
  trip_id string,
  pickup_datetime timestamp,
  dropoff_datetime timestamp,
  vendor_id string,
  passenger_count int,
  trip_distance double,
  fare_amount double
)
USING iceberg
LOCATION 'file:///tmp/iceberg_warehouse/iceberg_trips';
```

Ou via API PySpark:

```python
df.writeTo("local_iceberg.default.iceberg_trips").create()
```

## Exemplos de operações

### INSERT
```python
new_df.writeTo("local_iceberg.default.iceberg_trips").append()
```

### UPDATE
```sql
UPDATE local_iceberg.default.iceberg_trips
SET fare_amount = fare_amount * 1.05
WHERE pickup_borough = 'Manhattan';
```

### DELETE
```sql
DELETE FROM local_iceberg.default.iceberg_trips
WHERE passenger_count = 0;
```

### MERGE
```sql
MERGE INTO local_iceberg.default.iceberg_trips t
USING updates s
ON t.trip_id = s.trip_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```