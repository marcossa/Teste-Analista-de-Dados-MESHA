# Teste Analista de Dados
Critérios avaliadas:
- Uso de Funções DAX
- Documentação das medidas
- ETL
- Modelagem dimensional dos dados

### Desejáveis
- Esquema Estrela
- Criação de visuais com indicadores além dos requisitados.  
[Teste-Analista-de-Dados-MESHA-marcossa](https://github.com/marcossa/Teste-Analista-de-Dados-MESHA/blob/Teste-Mesha/docs/Teste-Analista-de-Dados-MESHA-marcossa.pdf)  
- SQL (Caso deseje modelar os dados em algum banco)


### Steps:

1. Realizar um Fork desse projeto
2. Realizar a modelagem dimensional da base (Pode ser dentro do próprio PowerBI ou outra ferramenta de ETL)
    - A base está disponível para download [clicando aqui](https://download.inep.gov.br/microdados/microdados_enem_2020.zip).
    - Após descompactar a paste, o Arquivo com a base encontra-se no diretório microdados_enem_2020/DADOS/MICRODADOS_ENEM_2020.csv
    - A documentação necessária sobre os campos da base está disponível nos demais diretórios dentro da pasta descompactada.
4. Disponibilizar o link do seu repositório para posterior avaliação


### Levantar Indicadores
#### Responder às seguintes perguntas:
1. Qual a escola com a maior média de notas?
- `Escola/Município: 3158904.0 - Santana do Manhuaçu/MG`
- `Média de Notas da Escola/Município: 706,56`
- `Número de inscritos: 1`
2. Qual o aluno com a maior média de notas e o valor dessa média?
- `Inscrição: 200005996961`
- `Média Individual: 858,58`
- `Escola/Município: Não Declarado`
3. Qual a média geral?
- `Média Geral: 530,55`
4. Qual o % de Ausentes?
- `Número de Ausentes no primeiro dia de prova: 3.184.243`
- `Número de Ausentes no segundo dia de prova: 3.024.590`
- `Percentual de Ausentes em pelo menos um dos dias de prova: 55,21%`
5. Qual o número total de Inscritos?
- `Número Total de Inscritos: 5.783.109`
6. Qual a média por disciplina?
*Média geral por Área do Conhecimento:*
`CN-Ciências da Natureza: 491,74`
`CH-Ciências Humanas: 515,98`
`LC-Linguagens e Códigos: 527,66`
`MT-Matemática: 522,48`
`Redação: 594,87`
7. Qual a média por Sexo?
*Média geral por sexo:*
- `F: 524,61`
- `M: 539,70`
8. Qual a média por Etnia?
*Média geral por etnia:*
- `0-Não declarado: 539,36`
- `1-Branca: 559,55`
- `2-Preta: 505,10`
- `3-Parda: 512,98`
- `4-Amarela: 528,60`
- `5-Indígena: 480,23`


---
### Respostas obtidas em Python
- **Número total de inscritos:** `5.783.109`
- **Número de ausentes no primeiro dia de prova:** `3.184.243`
- **Número de ausentes no segundo dia de prova:** `3.024.590`
- **Percentual de ausentes em pelo menos um dos dias de prova:** `55.21%`  
- **Média geral:** `530.55`

- **Média geral por área do conhecimento:**  
`NU_NOTA_CN         491.743250`  
`NU_NOTA_CH         515.977130`  
`NU_NOTA_LC         527.658998`  
`NU_NOTA_MT         522.484363`  
`NU_NOTA_REDACAO    594.866780`  

- **Média geral por etnia:**
*TP_COR_RACA*  
`0    539.359489`  
`1    559.545128`  
`2    505.093910`  
`3    512.981683`  
`4    528.601207`  
`5    480.225743`  

- **Média geral por sexo:**
*TP_SEXO*  
`F    524.607044`  
`M    539.695145`  

- **Ranking das 10 escolas com as maiores médias de notas:**


| **#** | **CO_MUNICIPIO_ESC** | **NO_MUNICIPIO_ESC**         | **SG_UF_ESC** | **Média** | **Inscritos** |
|-------|----------------------|------------------------------|---------------|-----------|---------------|
| 1.    | 3158904.0            | Santana do Manhuaçu          | MG            |    706.56 |             1 |
| 2.    | 4313466.0            | Novo Xingu                   | RS            |    704.90 |             1 |
| 3.    | 4305850.0            | Coqueiros do Sul             | RS            |    693.52 |             1 |
| 4.    | 4117297.0            | Novo Itacolomi               | PR            |    692.70 |             1 |
| 5.    | 3107000.0            | Biquinhas                    | MG            |    685.64 |             1 |
| 6.    | 3147808.0            | Passa Vinte                  | MG            |    681.74 |             2 |
| 7.    | 3160009.0            | Santo Antônio do Aventureiro | MG            |    670.80 |             1 |
| 8.    | 3170651.0            | Vargem Grande do Rio Pardo   | MG            |    668.77 |             3 |
| 9.    | 3149408.0            | Pedro Teixeira               | MG            |    656.16 |             1 |
| 10.   | 4304853.0            | Carlos Gomes                 | RS            |    654.44 |             2 |


- **Ranking das 10 maiores médias individuais:**


| **#** | **NU_INSCRICAO** | **MEDIA_NOTAS** | **ESCOLA**                    |
|-------|------------------|-----------------|-------------------------------|
| 1.    | 200005996961     |  858.58         |                           NaN |
| 2.    | 200004812135     |  852.86         |                           NaN |
| 3.    | 200001357436     |  852.76         | 3304557.0 - Rio de Janeiro/RJ |
| 4.    | 200004002694     |  851.50         |                           NaN |
| 5.    | 200001850224     |  851.34         |      3550308.0 - São Paulo/SP |
| 6.    | 200006051511     |  850.74         |    2507507.0 - João Pessoa/PB |
| 7.    | 200003688741     |  849.34         |                           NaN |
| 8.    |200006619550      |  847.82         |                           NaN |
| 9.    | 200001993301     |  847.68         |                           NaN |
| 10.   | 200004146848     |  847.60         |                           NaN |


### Análise da documentação
Numa análise preliminar dos dados e com base na documentação nota-se que:
1. Embora os dados estejam muito bem estruturados e documentados, encontram-se num único arquivo CSV, em colunas contíguas, cujas seções são indicadas por uma linha descritiva mesclada na documentação em análise.
	1.1 Qual a abordagem mais adequada para segmentar as colunas e derivar as respectivas tabelas para a análise dimensional?
		a) **Criar um script para segregar os dados conforme instruções;** ou
		b) Utlizar os recursos do Power Query e Linguagem M do PowerBI para fazê-lo.
2. As colunas C e D da documentação (quando preenchidas) decodificam as variáveis categóricas utilizadas na base de dados.
	2.1 Como extrair da documentação a interpretação dos valores numéricos?
		a) **Derivar da própria documentação as tabelas auxiliares no modelo dimensional;** ou
		b) Preencher essas tabelas manualmente, visto que são valores estáticos.
3. Em que pese o arquivo CSV conter apenas os dados referentes às provas do ENEM realizadas no ano 2020, como sugere a própria origem dos dados, bem como o valor único presente na coluna **NU_ANO** dando a esta caráter meramente descritivo, não está descartada a possibilidade de agregação de resultados de outras edições do ENEM, criando a dimensão temporal ausente nesta base de dados.


### Diário de bordo
A dificuldade no manejo do arquivo CSV único com tamanho de 2GB me levou a converter a base para o formato Parquet após diversos travamentos do PC.

O tamanho do arquivo foi reduzido para 475 MB, mas persistiu a dificuldade de carregar dados do Power Query para o Power BI.

Optei então pela segmentação do arquivo em arquivos menores correspondentes às seções definidas na documentação:
- Dados do Participante
- Dados da Escola
- Dados do Local de Aplicação da Prova
- Dados da Prova Objetiva
- Dados da Redação
- Dados do Questionário Sócio-Econômico

Mesmo após essas intervenções, apesar de melhorria no manejo dos arquivos, a lentidão na carga de dados persistiu.


### Algumas anotações  
    8.508 participantes faltaram no primeiro dia mas estiveram presentes ou foram eliminados no segundo dia  
  168.161 participantes estiveram presentes ou foram eliminados no primeiro dia mas faltaram no segundo dia  
  176.669 participantes faltaram a pelo menos um dos dias  
3.016.082 participantes faltaram em ambos os dias  


### Resolvendo problemas de performance
Refiz a segmentação desta vez predefinindo as colunas e mesclando as seções das Provas Objetiva e Redação
- Dados do Participante
- Dados da Escola
- Dados do Local de Aplicação da Prova
- Dados das Provas (Prova Objetiva e Redação)
- Dados do Questionário Sócio-Econômico


O arquivo Parquet correspondente às provas teve uma redução significativa em seu tamanho, passando de 360+43 MB para 67 MB

Uma análise exploratória de notas pelo perfil socioeconômico pode revelar novos insights

Os dados sobre as escolas são precários porque a indicação é opcional