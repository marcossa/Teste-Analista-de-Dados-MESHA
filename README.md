# Análise da documentação encontrada na planilha **MICRODADOS_ENEM_2020** da pasta de trabalhho **Dicionário_Microdados_Enem_2020.[ods|xlsx]** na pasta **DICIONÁRIO**

Numa análise preliminar dos dados e com base na documentação nota-se que:
1. Embora os dados estejam muito bem estruturados e documentados, encontram-se num único arquivo CSV, em colunas contíguas, cujas seções são indicadas por uma linha descritiva mesclada na documentação em análise.
	1.1 Qual a abordagem mais adequada para segmentar as colunas e derivar as respectivas tabelas para a análise dimensional?
		a) Criar um script para segregar os dados conforme instruções; ou
		b) Utlizar os recursos do Power Query e Linguagem M do PowerBI para fazê-lo.
2. As colunas C e D da documentação (quando preenchidas) decodificam as variáveis categóricas utilizadas na base de dados.
	2.1 Como extrair da documentação a interpretação dos valores numéricos?
		a) Derivar da própria documentação as tabelas auxiliares no modelo dimensional; ou
		b) Preencher essas tabelas manualmente, visto que são valores estáticos.
3. Em que pese o arquivo CSV conter apenas os dados referentes às provas do ENEM realizadas no ano 2020, como sugere a própria origem dos dados, bem como o valor único presente na coluna **NU_ANO** dando a esta caráter meramente descritivo, não está descartada a possibilidade de agregação de resultados de outras edições do ENEM, criando a dimensão temporal ausente nesta base de dados.


Analisando o tempo de atualização para decidir pelo fracionamento dos dados 
>> 

Inscrição => NF
Área      => Produto

    8.508 participantes faltaram no primeiro dia mas estiveram presentes ou foram eliminados no segundo dia
  168.161 participantes estiveram presentes ou foram eliminados no primeiro dia mas faltaram no segundo dia
  -------
  176.669 participantes que faltaram a pelo menos um dos dias
3.016.082 participantes que faltaram em ambos os dias

A dificuldade no manejo de um arquivo CSV único com tamanho de 2GB me levou a converter a base para o formato Parquet.
O tamanho do arquivo foi reduzido para 475 MB, mas persistiu a dificuldade de carregar dados do Power Query para o Power BI.
Segmentei o arquivo único em arquivos menores correspondentes às seções definidas na documentação:
- Dados do Participante
- Dados da Escola
- Dados do Local de Aplicação da Prova
- Dados da Prova Objetiva
- Dados da Redação
- Dados do Questionário Sócio-Econômico
Mesmo após essas intervenções, apesar de melhorria no manejo dos arquivos, a lentidão na carga de dados persistiu.

Refiz a segmentação desta vez predefinindo as colunas e mesclando as seções das Provas Objetiva e Redação
- Dados do Participante
- Dados da Escola
- Dados do Local de Aplicação da Prova
- Dados das Provas (Prova Objetiva e Redação)
- Dados do Questionário Sócio-Econômico
O arquivo Parquet correspondente às provas teve uma redução significativa em seu tamanho, passando de 360+43 MB para 67 MB

Uma análise exploratória de notas pelo perfil socioeconômico pode revelar novos insights

Os dados sobre as escolas são precários porque a indicação é opcional