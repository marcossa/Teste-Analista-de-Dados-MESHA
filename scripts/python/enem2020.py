import pandas as pd

# Carregar o arquivo Parquet
parquet_file_path = '/home/marcossa/Downloads/microdados_enem_2020/DADOS/microdados_enem_2020.parquet'
df = pd.read_parquet(parquet_file_path)

# Lista de colunas de notas
colunas_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

# Criar uma nova coluna com a média das notas, ignorando valores ausentes
df['MEDIA_NOTAS'] = df[colunas_notas].mean(axis=1, skipna=True)

# Filtrar com presença em ambos os dias de prova e que não foram eliminados
df_presentes = df[(df['TP_PRESENCA_CN'] == 1) & (df['TP_PRESENCA_LC'] == 1) & (df['TP_STATUS_REDACAO'] == 1)]

# Número total de inscritos
num_inscritos = df.shape[0]

# Número de ausentes no primeiro dia de prova
num_ausentes_primeiro_dia = df[df['TP_PRESENCA_CN'] == 0].shape[0]

# Número de ausentes no segundo dia de prova
num_ausentes_segundo_dia = df[df['TP_PRESENCA_LC'] == 0].shape[0]

# Percentual de ausentes em pelo menos um dos dias de prova
num_ausentes_pelo_menos_um_dia = df[(df['TP_PRESENCA_CN'] == 0) | (df['TP_PRESENCA_LC'] == 0)].shape[0]
percentual_ausentes_pelo_menos_um_dia = (num_ausentes_pelo_menos_um_dia / num_inscritos) * 100

# Média geral
media_geral = df_presentes['MEDIA_NOTAS'].mean()

# Média geral por área do conhecimento
media_por_area = df_presentes[colunas_notas].mean()

# Média geral por etnia
media_por_etnia = df_presentes.groupby('TP_COR_RACA')[colunas_notas].mean().mean(axis=1)

# Média geral por sexo
media_por_sexo = df_presentes.groupby('TP_SEXO')[colunas_notas].mean().mean(axis=1)

# Concatenar CO_MUNICIPIO_ESC com NO_MUNICIPIO_ESC
df_presentes['ESCOLA'] = df_presentes['CO_MUNICIPIO_ESC'].astype(str) + " - " + df_presentes['NO_MUNICIPIO_ESC'] + "/" + df_presentes['SG_UF_ESC']

# Calcular a média das notas por escola
media_notas_escola = df_presentes.groupby('ESCOLA')['MEDIA_NOTAS'].mean()

# Calcular o número de inscritos por escola
num_inscritos_escola = df_presentes['ESCOLA'].value_counts()

# Identificar as 10 escolas com as maiores médias de notas
top_10_escolas = media_notas_escola.nlargest(10).index
top_10_medias = media_notas_escola.nlargest(10).values

# Ranking dos 10 alunos com as maiores médias individuais de notas
top_10_alunos = df_presentes.nlargest(10, 'MEDIA_NOTAS')[['NU_INSCRICAO', 'MEDIA_NOTAS', 'ESCOLA']]

# Participante com a maior média de notas identificado pelo NU_INSCRICAO
#participante_maior_media = df_presentes.loc[df_presentes['MEDIA_NOTAS'].idxmax()]
#maior_media_notas = participante_maior_media['MEDIA_NOTAS']
#numero_inscricao_maior_media = participante_maior_media['NU_INSCRICAO']

# Exibir resultados
print(f"Número total de inscritos: {num_inscritos}")
print(f"Número de ausentes no primeiro dia de prova: {num_ausentes_primeiro_dia}")
print(f"Número de ausentes no segundo dia de prova: {num_ausentes_segundo_dia}")
print(f"Percentual de ausentes em pelo menos um dos dias de prova: {percentual_ausentes_pelo_menos_um_dia:.2f}%")
print(f"Média geral: {media_geral:.2f}")
print("Média geral por área do conhecimento:")
print(media_por_area)
print("Média geral por etnia:")
print(media_por_etnia)
print("Média geral por sexo:")
print(media_por_sexo)
print("\nRanking das 10 escolas com as maiores médias de notas:")
for i, escola in enumerate(top_10_escolas):
    print(f"{i+1}. {escola}: Média = {top_10_medias[i]:.2f}, Número de inscritos = {num_inscritos_escola[escola]}")
#print(f"Participante com a maior média de notas: {numero_inscricao_maior_media}, Média: {maior_media_notas:.2f}")
print(top_10_alunos.to_string(index=False))