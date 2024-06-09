import pyarrow.parquet as pq
import pyarrow as pa
import os

path_parquets = 'microdados_enem_2020'
path_combined_parquet = 'microdados_enem_2020.parquet'

# Lista os arquivos Parquet criados
chunk_files = [f for f in os.listdir() if f.startswith(path_parquets) and f.endswith('.parquet')]
chunk_files.sort()

# Combina os arquivos Parquet em um único arquivo
tables = [pq.read_table(f) for f in chunk_files]
combined_table = pa.concat_tables(tables)
pq.write_table(combined_table, path_combined_parquet)

print("Arquivos Parquet combinados com sucesso!")

