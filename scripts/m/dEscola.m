let
    Fonte = Parquet.Document(File.Contents("file:///D:/microdados_enem_2020/DADOS/microdados_enem_2020_escola.parquet"), [Compression=null, LegacyColumnNameEncoding=false, MaxDepth=null]),
    #"Remover Vazios" = Table.SelectRows(Fonte, each [CO_MUNICIPIO_ESC] <> null and [CO_MUNICIPIO_ESC] <> ""),
    #"Tipos Alterados" = Table.TransformColumnTypes(#"Remover Vazios",{{"CO_MUNICIPIO_ESC", Int64.Type}, {"NO_MUNICIPIO_ESC", type text}, {"CO_UF_ESC", Int64.Type}, {"SG_UF_ESC", type text}, {"TP_DEPENDENCIA_ADM_ESC", Int64.Type}, {"TP_LOCALIZACAO_ESC", Int64.Type}, {"TP_SIT_FUNC_ESC", Int64.Type}}),
    #"Consultas Mescladas1" = Table.NestedJoin(#"Tipos Alterados", {"TP_DEPENDENCIA_ADM_ESC"}, cDependenciaAdmEscola, {"TP_DEPENDENCIA_ADM_ESC"}, "cDependenciaAdmEscola", JoinKind.LeftOuter),
    #"cFaixaEtaria Expandido" = Table.ExpandTableColumn(#"Consultas Mescladas1", "cDependenciaAdmEscola", {"Dependência Adm. Escola"}, {"Dependência Adm. Escola"}),
    #"Consultas Mescladas2" = Table.NestedJoin(#"cFaixaEtaria Expandido", {"TP_LOCALIZACAO_ESC"}, cLocalizacaoEscola, {"TP_LOCALIZACAO_ESC"}, "cLocalizacaoEscola", JoinKind.LeftOuter),
    #"cLocalizacaoEscola Expandido" = Table.ExpandTableColumn(#"Consultas Mescladas2", "cLocalizacaoEscola", {"Localização da Escola"}, {"Localização da Escola"}),
    #"Consultas Mescladas3" = Table.NestedJoin(#"cLocalizacaoEscola Expandido", {"TP_SIT_FUNC_ESC"}, cSituacaoFuncEscola, {"TP_SIT_FUNC_ESC"}, "cSituacaoFuncEscola", JoinKind.LeftOuter),
    #"cSituacaoFuncEscola Expandido" = Table.ExpandTableColumn(#"Consultas Mescladas3", "cSituacaoFuncEscola", {"Situação Funcionamento da Escola"}, {"Situação Funcionamento da Escola"})
in
    #"cSituacaoFuncEscola Expandido"