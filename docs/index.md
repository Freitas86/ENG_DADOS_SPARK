# Documentação do Projeto

Este projeto demonstra como configurar um ambiente de **PySpark** com suporte ao **Delta Lake** e **Apache Iceberg**, utilizando **Poetry** como gerenciador de pacotes.

## Estrutura

- `src/` → código fonte (configuracao do Spark e utilitarios)
- `notebooks/` → notebooks com exemplos de carga, DDL e comandos INSERT/UPDATE/DELETE
- `docs/` → documentação gerada pelo MkDocs
- `README.md` → instruções de uso
- `pyproject.toml` → dependências gerenciadas pelo Poetry

## Como rodar

1. Instale dependências:
   ```bash
   poetry install
   poetry shell
   ```

2. Baixe os dados (NYC TLC Green Taxi):
   ```bash
   mkdir data
   curl -o data/green_tripdata_sample.csv "https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2022-01.csv"
   ```

3. Inicie o JupyterLab com os pacotes Delta e Iceberg:
   ```bash
   export SPARK_PACKAGES="io.delta:delta-core_2.12:2.2.0,org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0"
   PYSPARK_SUBMIT_ARGS="--packages $SPARK_PACKAGES pyspark-shell" jupyter lab
   ```

4. Execute os notebooks dentro da pasta `notebooks/`.

5. Para abrir a documentação local:
   ```bash
   mkdocs serve
   ```
