<!-- TOC -->

- [1. VBA EXCEL](#1-vba-excel)
    - [1.1. Como inicializar sua macro para Otimizá-la?](#11-como-inicializar-sua-macro-para-otimizá-la)
    - [Método que verifica se Aba Existe na Planilha](#método-que-verifica-se-aba-existe-na-planilha)

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

## Método que verifica se Aba Existe na Planilha

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