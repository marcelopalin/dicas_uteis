# 1. Python 3.6+

## Criando Ambiente Virtual no Linux/Windows

Crie um ambiente virtual em Python 3
Crie um ambiente virtual no Python 3 com o nome do ambiente **env**:

virtualenv -p python3 env

## Valide que o ambiente está instalado com o python3:

ls env/lib

## Ativar Ambiente
Ative o ambiente virtual recém-criado (o nome do ambiente de trabalho aparecerá entre parênteses):

source env/bin/activate

(env) testuser@localhost:~/python-environments$

Agora que o ambiente está ativo, você pode instalar executáveis ​​e pacotes somente neste ambiente virtual.

## Desativar Ambiente
Para desativar um ambiente virtual ativo:

deactivate


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


### Como saber qual é o sistema operacional que o script está rodando?

Utilize:

```python
def get_platform():
    """
    Objetivo: padronizar a descoberta dos sistema operacional
    em apenas 3 respostas: windows, linux e macosx.
    Muito utilizado para trabalhar com diretórios.

    Imports: sys
    """
    platforms = {
        'linux1': 'linux',
        'linux2': 'linux',
        'darwin': 'macosx',
        'win32': 'windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]
```

Modo de utilizar: 

```python
import sys

print(get_platform())

if get_platform = 'linux':
    print("Você está no linux!")

```


### Como criar um arquivo vazio utilizando o PATHLIB - Python 3.6+?

Simplesmente faça:

```python
from pathlib import Path

Path('arquivo_vazio.txt').touch()

```

### Como baixar um arquivo com requests?

Para uma maior sofisticação do seu código vamos definir o timeout de 5 segundos
para aguardar a conexão com o servidor. 

Vamos verificar o tamanho do arquivo a ser baixado e depois de baixado vamos
fazer a verificação se bate com o tamanho.

```python
        
        url = 'https://www.peterbe.com/unzip-in-parallel/symbols-2017-11-27T14_15_30.zip'
        r = requests.head(url, timeout=(5, 14))

        # Security: link is avalible?
        if not r.status_code == 200:
            print("=" * 80)
            print(" Script Interrupted!")
            print(" Url do arquivo do ETA40 do ONS {} não está disponível!".format(url))
            print("=" * 80)
            logger.info(" Script Interrupted! ")
            logger.info(" Url do arquivo do ETA40 do ONS {} não está disponível!".format(url))
            sys.exit(0)        
 
        print(json.dumps(r.json(), indent=4, sort_keys=True))

    except requests.exceptions.ConnectTimeout as err:
        print('ERRO de TIME OUT!!')
    except requests.exceptions.ReadTimeout as err:
        print('ERRO READTIMEOUT de TIME OUT!!')
    except requests.exceptions.HTTPError as err:
        print ("Http Error:",err)
    except requests.exceptions.ConnectionError as err:
        print ("Error Connecting:",err)
    except requests.exceptions.Timeout as err:
        print ("Timeout Error:",err)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)    

```


### Imprimindo o tamanho do arquivo a ser baixado?

Para uma maior sofisticação do seu código vamos definir o timeout de 5 segundos
para aguardar a conexão com o servidor. 

Vamos verificar o tamanho do arquivo a ser baixado e depois de baixado vamos
fazer a verificação se bate com o tamanho.

```python
    r = requests.get('http://repositorio.ipea.gov.br/bitstream/11058/3532/9/cc13_serieshistoricas.xls', timeout=5)
    
    # Imprimindo a resposta
    # print(json.dumps(r.json(), indent=4, sort_keys=True))

    # Print File Size
    size_of_file_bytes =  r.headers['Content-length']
    print('Tamanho do arquivo no site: {} bytes '.format(size_of_file_bytes))

```


