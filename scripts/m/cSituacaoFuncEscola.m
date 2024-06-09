let
    Fonte = Excel.Workbook(File.Contents("D:\microdados_enem_2020\DICIONÁRIO\Dicionário_Microdados_Enem_2020.xlsx"), null, false),
    MICRODADOS_ENEM_2020_sheet = Fonte{[Item="MICRODADOS_ENEM_2020",Kind="Sheet"]}[Data],
    #"Preenchido Abaixo" = Table.FillDown(MICRODADOS_ENEM_2020_sheet,{"Column1"}),
    #"Linhas Filtradas" = Table.SelectRows(#"Preenchido Abaixo", each ([Column1] = "TP_SIT_FUNC_ESC")),
    #"Outras Colunas Removidas" = Table.SelectColumns(#"Linhas Filtradas",{"Column3", "Column4"}),
    #"Colunas Renomeadas" = Table.RenameColumns(#"Outras Colunas Removidas",{{"Column3", "TP_SIT_FUNC_ESC"}, {"Column4", "Situação Funcionamento da Escola"}}),
    #"Tipo Alterado" = Table.TransformColumnTypes(#"Colunas Renomeadas",{{"TP_SIT_FUNC_ESC", Int64.Type}, {"Situação Funcionamento da Escola", type text}})
in
    #"Tipo Alterado"