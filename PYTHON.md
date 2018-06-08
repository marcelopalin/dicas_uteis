# Dicas Python

## Leitura de um Arquivo CSV - Python 3.6+

Objetivo:

Colocar os dados lidos do CSV em uma lista de dicionários, ou seja, algo assim:

[{'id': '1', 'nome': 'Palin', 'login': 'palin@mail.com', 'pass': 'teste'}, {'id': '2', 'nome': 'Daniel', 'login': 'd@mail.com', 'pass': 'd1234343'}]

O comando que faz isso é:

```
    with open("Entrada/Informacoes_Rede_Basica_formato_BD.csv", "r", encoding='utf-8', errors='ignore', newline='') as f:
        reader = csv.DictReader(f, delimiter=";")
        lst_of_dicts = map(dict)
```

Saída:

```python
[{'\ufeffid': '1', 'nome': 'Palin', 'login': 'palin@mail.com', 'pass': 'teste'}, {'id': '2', 'nome': 'Daniel', 'login': 'd@mail.com', 'pass': 'd1234343'}]
```

Temos um problema de conversão de caracteres e ao tentarmos acessar a chave da coluna inicial dará o seguinte erro: **KeyError: 'id'**.
Ou seja, você não consegue acessar a chave 'id'. 
Solução, fazer um loop pelos dicionários lidos e inserindo a chave novamente com o código:

```python
        for d in map(dict, reader):
            #print(d)
            print(d['id']) # Problema a Key 'id' vem como sendo '\ufeffid'
            #Se tentar acessar a chave 'id' dará erro!
            #Solucao:
            d['id'] = d[reader.fieldnames[0]]
```


Porém, gostaria de transformar novamente em um dicionário indexado pelo 'id', ou seja, em algo assim:

[{'id': '1', 'nome': 'Palin', 'login': 'palin@mail.com', 'pass': 'teste'}, {'id': '2', 'nome': 'Daniel', 'login': 'd@mail.com', 'pass': 'd1234343'}]


```python
    with open("Entrada/dados.csv", "r", encoding='utf-8', errors='ignore', newline='') as f:
        reader = csv.DictReader(f, delimiter=";")

        # Pode usar for d in map(dict, reader) ou for d in reader:
        for d in reader:
            # Acrescenta a Key 'id' com o valor do campo
            #d['id'] = int(d[reader.fieldnames[0]])
            lst_dict.append(d)

    #Transforma a lista de dicionários em um Dicionário onde você pode buscar a linha pelo Key desejada, neste caso "id"
    dic_dados = build_dict(lst_dict, key="id")            
```

Método que converte a lista de dicionários em um dicionário com a Key desejada, neste caso:

```python
    def build_dict(seq, key):
        """
            Monta uma Lista de Dicionarios em um Dicionario com Key que você define
            Ex: [{'id': 1, 'nome': 'Marcelo'},{'id': 2, 'nome': 'Pedrinho'}]
            transforma em: {1: {'id': 1, 'nome': 'Marcelo'}, 2: {'id': 2, 'nome': 'Pedrinho'}}
            :param seq:
            :param key:
            :return:
        """
        return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))
```