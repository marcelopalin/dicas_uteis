<!-- TOC -->

- [1. VBA EXCEL](#1-vba-excel)
    - [1.1. Como inicializar sua macro para Otimizá-la?](#11-como-inicializar-sua-macro-para-otimizá-la)
    - [1.2. Método que verifica se Aba Existe na Planilha](#12-método-que-verifica-se-aba-existe-na-planilha)
    - [1.3. Verificar se uma Tabela (object) do Excel existe](#13-verificar-se-uma-tabela-object-do-excel-existe)

<!-- /TOC -->

# 1. VBA EXCEL

## 1.1. Como inicializar sua macro para Otimizá-la?

```
    On Error Resume Next
    With Application
       .ScreenUpdating = False
       .EnableEvents = False
       .Calculation = xlCalculationManual
    End With
```

No final não esqueça de colocar:

```
    With Application
        .ScreenUpdating = True
        .EnableEvents = True
        .Calculation = xlCalculationAutomatic
    End With
```

## 1.2. Método que verifica se Aba Existe na Planilha

```
Public Function aba_existe(wb As Workbook, strNameWsheet As String)
    
    Dim strGetName As String
    
    On Error Resume Next
    strGetName = wb.Worksheets(strNameWsheet).Name
    If Err.Number = 0 Then
        aba_existe = True
    Else
        Err.Clear
        aba_existe = False
    End If
End Function
```

Exemplo de uso:

```
    Dim wb As Workbook
    Set wb = ThisWorkbook

    Dim sNomeAba as String
    sNomeAba = "Clientes"

    Dim chk_aba As Boolean
    chk_aba = aba_existe(wb, sNomeAba)
    If chk_aba = False Then
        MsgBox "A Aba " & sNomeAba & " NÃO FOI ENCONTRADA! ", vbCritical
    Exit Sub
    End If
```


## 1.3. Verificar se uma Tabela (object) do Excel existe

```
    Dim sNomeAba as String
    sNomeAba = "Clientes"

    Dim sNomeTblExcel As String
    Dim ListObj As ListObject
    sNomeTblExcel = "tbl_dados_clientes"

    'Varre a lista de objetos
    For Each ListObj In wb.Sheets(sNomeAba).ListObjects
        If ListObj.Name = sNomeTblExcel Then
            ListObj.AutoFilter.ShowAllData 'remove os filtros
        End If
    Next ListObj
```