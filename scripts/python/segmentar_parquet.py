import pandas as pd
import sys

# Definir o nome do arquivo Parquet completo (sem a extensão .parquet)
prefix_parquet = sys.argv[1]

# Carregar o arquivo Parquet completo
df = pd.read_parquet(f"{prefix_parquet}.parquet")

# Definir as seções e respectivas colunas
segmentos = {
	'participante': ['NU_INSCRICAO', 'NU_ANO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO', 'IN_TREINEIRO'],
	'escola': ['CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC'],
	'local': ['NU_INSCRICAO', 'NU_ANO', 'CO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA'],
	'provas': ['NU_INSCRICAO', 'NU_ANO', 'CO_MUNICIPIO_ESC', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_REDACAO'],
	'socioEconomico': ['NU_INSCRICAO', 'NU_ANO', 'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013', 'Q014', 'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022', 'Q023', 'Q024', 'Q025']
}

# Função para segmentar e salvar os dados
def segmentar(df, segmentos, pathBase='./'):
  for segmento, colunas in segmentos.items():
    df_segmento = df[colunas]
    pathSegmento = f"{pathBase}{prefix_parquet}_{segmento}.parquet"
    df_segmento.to_parquet(pathSegmento, index=False)
    print(f"Segmento {segmento} salvo como {pathSegmento}")

segmentar(df, segmentos)

print("Arquivo Parquet segmentado com sucesso!")

