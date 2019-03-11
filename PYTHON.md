# 1. Python 3.6+

## 1.1. Trabalhando com Zip

Importação padrão:

```python
import zipfile
import os
```

### 1.1.1. Método II - compactando um diretorio para um arquivo Zip

Vamos utilizar como exemplo a seguinte estrutura de diretórios (DirOrigem):

```bash
DirOrigem/
|
├── dir01
│   ├── arq01.dat
│   ├── arq02.dat
│   ├── f001.txt
│   ├── f002.txt
│   └── f003.txt
└── dir02
    ├── a001.txt
    ├── a002.txt
    └── f.zip

2 directories, 5 files
```

```python
def zipDirToFile(dir, zip_file):
    zip = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED)
    root_len = len(os.path.abspath(dir))
    for root, dirs, files in os.walk(dir):
        archive_root = os.path.abspath(root)[root_len:]
        for f in files:
            fullpath = os.path.join(root, f)
            archive_name = os.path.join(archive_root, f)
            zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
    zip.close()
    return zip_file
```

Compactando o diretório **DirOrigem**:

```bash

```



### 1.1.2.  Verificando se é um arquivo Zip Válido

```python
def isZipFile(zip_file_name):
  return zipfile.is_zipfile(zip_file_name)
```

### 1.1.2.  Retornando a lista de arquivos dentro do Zip

```python
def getListFilesFromZip(zip_file_name):
  zf = zipfile.ZipFile(zip_file_name)
  return zf.namelist()
```


## 1.2. Leitura de um Arquivo CSV - Python 3.6+

Objetivo:

Colocar os dados lidos do CSV em uma lista de dicionários, ou seja, algo assim:

[{'id': '1', 'nome': 'Palin', 'login': 'palin@mail.com', 'pass': 'teste'}, {'id': '2', 'nome': 'Daniel', 'login': 'd@mail.com', 'pass': 'd1234343'}]

O comando que faz isso é:

```bash
    with open("Entrada/Informacoes_Rede_Basica_formato_BD.csv", "r", encoding='utf-8', errors='ignore', newline='') as f:
        reader = csv.DictReader(f, delimiter=";")
        lst_of_dicts = map(dict)
```

**Saída:**

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