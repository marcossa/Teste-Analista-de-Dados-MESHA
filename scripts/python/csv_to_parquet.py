import pandas as pd
import sys
import os

# Definir o caminho do arquivo CSV e o nome do arquivo Parquet de destino
path_csv = sys.argv[1]
path_parquet = sys.argv[2]
chunk_size = 100000 # Tamanho do chunk para evitar travamento

# Primeira leitura para determinar o schema
df_sample = pd.read_csv(path_csv, delimiter=';', encoding='latin1', nrows=chunk_size)
schema = df_sample.dtypes
  
# Carregar o arquivo CSV
#df = pd.read_csv(path_csv, delimiter=';', encoding='latin1')

#Processamento do CSV em chunks
for i, chunk in enumerate(pd.read_csv(path_csv, delimiter=';', encoding='latin1', chunksize=chunk_size)):
  # Validar o schema
  for col in schema.index:
    if col in chunk.columns:
      chunk[col] = chunk[col].astype(schema[col])
  chunk.to_parquet(f"{path_parquet}_chunk_{i}.parquet", index=False)

# Salvar o arquivo Parquet
#df.to_parquet(path_parquet, index=False)

print(f"Chunks do arquivo salvos como parquet. Combinar os arquivos em seguida...")
