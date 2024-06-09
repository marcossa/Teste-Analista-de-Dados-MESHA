# Teste Analista de Dados
Critérios avaliadas:
- Uso de Funções DAX
- Documentação das medidas
- ETL
- Modelagem dimensional dos dados

### Desejáveis
- Esquema Estrela
- Criação de visuais com indicadores além dos requisitados.
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
2. Qual o aluno com a maior média de notas e o valor dessa média?
3. Qual a média geral?
4. Qual o % de Ausentes?
5. Qual o número total de Inscritos?
6. Qual a média por disciplina?
7. Qual a média por Sexo?
8. Qual a média por Etnia?

---

### Análise da documentação
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
