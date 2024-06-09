let
    Fonte = Parquet.Document(File.Contents("file:///D:/microdados_enem_2020/DADOS/microdados_enem_2020_provas.parquet"), [Compression=null, LegacyColumnNameEncoding=false, MaxDepth=null]),
    #"Tipos Alterados" = Table.TransformColumnTypes(#"Fonte",{{"NU_INSCRICAO", type text}, {"NU_ANO", Int64.Type}, {"CO_MUNICIPIO_ESC", Int64.Type}, {"TP_PRESENCA_CN", Int64.Type}, {"TP_PRESENCA_CH", Int64.Type}, {"TP_PRESENCA_LC", Int64.Type}, {"TP_PRESENCA_MT", Int64.Type}, {"CO_PROVA_CN", Int64.Type}, {"CO_PROVA_CH", Int64.Type}, {"CO_PROVA_LC", Int64.Type}, {"CO_PROVA_MT", Int64.Type}, {"NU_NOTA_CN", type number}, {"NU_NOTA_CH", type number}, {"NU_NOTA_LC", type number}, {"NU_NOTA_MT", type number}, {"TP_STATUS_REDACAO", Int64.Type}, {"NU_NOTA_REDACAO", type number}}, "en-US"),
    #"Definir Colunas" = Table.SelectColumns(#"Tipos Alterados",{"NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_ESC", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "TP_STATUS_REDACAO", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"}),
    #"Nulos para Zero" = Table.ReplaceValue(#"Definir Colunas", null, 0, Replacer.ReplaceValue, {"TP_STATUS_REDACAO", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"}),
    #"Unpivot Notas por Área" = Table.UnpivotOtherColumns(#"Nulos para Zero", {"NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_ESC", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "TP_STATUS_REDACAO"}, "SG_AREA", "NOTA"),
    Trim = Table.TransformColumns(#"Unpivot Notas por Área", {{"SG_AREA", each Text.AfterDelimiter(_, "NU_NOTA_"), type text}}),
    #"Presença 01" = Table.AddColumn(Trim, "Presença Dia 01", each Number.BitwiseAnd([TP_PRESENCA_LC],[TP_PRESENCA_CH])),
    #"Presença 02" = Table.AddColumn(#"Presença 01", "Presença Dia 02", each Number.BitwiseAnd([TP_PRESENCA_MT],[TP_PRESENCA_CN])),
    #"Participantes Habilitados" = Table.AddColumn(#"Presença 02", "Habilitado", each ([Presença Dia 01] = 1 and [Presença Dia 02] = 1) and [TP_STATUS_REDACAO] = 1),
    #"Tipos Presença Alterados" = Table.TransformColumnTypes(#"Participantes Habilitados",{{"TP_STATUS_REDACAO", Int64.Type}, {"Presença Dia 01", Int64.Type}, {"Presença Dia 02", Int64.Type}})
in
    #"Tipos Presença Alterados"