# 1. Pathlib incluida na Base do Python 3.6+

**Referências:**

PEP 428
https://www.python.org/dev/peps/pep-0428/

https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

https://realpython.com/python-pathlib/

https://realpython.com/python-pathlib/#the-problem-with-python-file-path-handling

http://blog.danwin.com/using-python-3-pathlib-for-managing-filenames-and-directories/


## 1.1. Operações Comuns


## 1.2. SEM PATHLIB

```python
from glob import glob
from os import makedirs
from os.path import basename, join
from shutil import unpack_archive
import requests
# pretend DATA_URL could point to an archive file URL only known at runtime
# i.e. we don't know if it's a zip, gz, etc., which is why we use 
# unpack_archive instead of ZipFile
DATA_URL = 'http://stash.compciv.org/ssa_baby_names/names.zip' 
DATA_DIR = join('/', 'tmp', 'pathto', 'stuff')
ZIP_FNAME = join(DATA_DIR, basename(DATA_URL))
makedirs(DATA_DIR, exist_ok=True)
print('Downloading', DATA_URL)
resp = requests.get(DATA_URL)
with open(ZIP_FNAME, 'wb') as wf:
    print("Saving to", ZIP_FNAME)
    wf.write(resp.content)

unpack_archive(ZIP_FNAME, extract_dir=DATA_DIR)
for fname in glob(join(DATA_DIR,  '*.txt')):
    with open(fname, 'r') as rf:
        print(fname, rf.read())
```


## 1.3. COM PATHLIB

```python
from pathlib import Path
from shutil import unpack_archive
import requests

DATA_URL = 'http://stash.compciv.org/ssa_baby_names/names.zip' 
DATA_DIR = Path('/', 'tmp', 'pathto', 'stuff')
DATA_DIR.mkdir(exist_ok=True, parents=True)
ZIP_FNAME = DATA_DIR.joinpath(Path(DATA_URL).name)

print('Downloading', DATA_URL)
resp = requests.get(DATA_URL)
print("Saving to", ZIP_FNAME)
ZIP_FNAME.write_bytes(resp.content)

unpack_archive(str(ZIP_FNAME), extract_dir=str(DATA_DIR))
for fpath in DATA_DIR.glob('*.txt'):
    print(fpath, fpath.read_text())
```


## 1.4. Porque utilizar?

Here are some highlights that I have noticed in just a few days of playing with the pathlib.

# 2. Working with folders

>>> from pathlib import Path

## 2.1. Verificando se o diretório existe
>>> Path('docs').exists()
False

## 2.2. Criando o Diretório
>>> Path('docs').mkdir()

## 2.3. Verificando se é um diretório
>>> Path('docs').is_dir()
True

Listing all of the files in a folder
>>> Path('docs').glob('*.md')
<generator object Path.glob at 0x1128ee258>

# 3. Since generator output isn't obvious :)
>>> [item for item in Path('docs').glob('*.md')]
[PosixPath('docs/README.md')]
Working with files
>>> Path('docs', 'README.md').is_file()
True

>>> Path('docs').joinpath('README.md')
Opening a file
>>> Path('README.md').open('r').read()
Writing to a file
>>> Path('README.md').write_text('Read the Docs!')
Reading from file
>>> Path('README.md').read_text()
'Read the Docs!'
What about Python 2?
Even though pathlib is built into Python 3, there is a Python 2.7 backport for anyone who can’t switch yet.


# 4. ARTIGO II


## 4.1. o.path é desajeitado

O os.path módulo sempre foi o que buscamos para trabalhar com caminhos em Python. Tem praticamente tudo que você precisa, mas às vezes pode ser muito desajeitado.

Você deve importá-lo assim?

import os.path

```bash
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```

Ou assim?

```bash
from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))
TEMPLATES_DIR = join(BASE_DIR, 'templates')
```

Ou talvez essa join função seja genericamente nomeada ... então poderíamos fazer isso em vez disso:

```bash
from os.path import abspath, dirname, join as joinpath

BASE_DIR = dirname(dirname(abspath(__file__)))
TEMPLATES_DIR = joinpath(BASE_DIR, 'templates')
```

Eu acho tudo isso um pouco estranho. Estamos passando strings para funções que retornam strings, as quais passamos para outras funções que retornam strings. Todas essas strings representam caminhos, mas ainda são apenas strings.

As funções string-in-string-out os.path são realmente desajeitadas quando aninhadas porque o código tem que ser lido de dentro para fora. Não seria legal se pudéssemos fazer essas chamadas de função aninhadas e transformá-las em chamadas de método encadeadas?

Com o pathlib módulo podemos!

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')

```


O os.path módulo requer aninhamento de funções, mas a classe pathlibdos módulos Pathnos permite encadear métodos e atributos em Path objetos para obter uma representação de caminho equivalente.

Eu sei o que você está pensando: espere que esses Path objetos não sejam a mesma coisa: eles são objetos, não cordas de caminho! Vou abordar isso mais tarde (dica: isso pode ser usado de forma intercambiável com strings de caminho).

O módulo **os** está lotado
O os.path módulo clássico do Python é apenas para trabalhar com caminhos. Uma vez que você queira realmente fazer algo com um caminho (por exemplo, criar um diretório), você precisará procurar outro módulo Python, geralmente o osmódulo.

O **os** módulo tem muitas utilidades para trabalhar com arquivos e diretórios: mkdir, getcwd, chmod, stat, remove, rename, e rmdir. Além disso chdir, link, walk, listdir, makedirs, renames, removedirs, unlink(a mesma que remove), e symlink. E um monte de outras coisas que não está relacionado com os sistemas de arquivos em tudo: fork, getenv, putenv, environ, getlogin, e system. Mais dezenas de coisas que não mencionei neste parágrafo.

O **os** módulo do Python faz um pouco de tudo; é uma espécie de gaveta de lixo para coisas relacionadas ao sistema . Há muitas coisas bonitas no osmódulo, mas pode ser difícil encontrar o que você está procurando às vezes: se você está procurando por coisas relacionadas ao caminho ou relacionadas ao sistema de arquivos no osmódulo, você precisará fazer uma pouco de cavar.

O pathlibmódulo substitui muitos desses osutilitários relacionados ao sistema de arquivos por métodos no Pathobjeto.

Aqui está um código que faz um src/__pypackages__ diretório e **renomeia** nosso .editorconfig arquivo para src/.editorconfig:

```python
import os
import os.path

os.makedirs(os.path.join('src', '__pypackages__'), exist_ok=True)
os.rename('.editorconfig', os.path.join('src', '.editorconfig'))
```

Este código faz a mesma coisa usando Path objetos:

```python
from pathlib import Path

Path('src/__pypackages__').mkdir(parents=True, exist_ok=True)
Path('.editorconfig').rename('src/.editorconfig')
```


Observe que o pathlibcódigo coloca o caminho primeiro devido ao encadeamento do método!

Como o Zen of Python diz, “namespaces são uma grande ideia, vamos fazer mais daquelas”. O osmódulo é um namespace muito grande com um monte de coisas nele. A classe pathlib.Path é um namespace muito menor e mais específico que o módulo os . Além disso, os métodos neste Pathnamespace retornam Pathobjetos, o que permite o encadeamento de métodos em vez de chamadas de função string-iful aninhadas.

Não se esqueça do módulo glob!
Os módulos ose os.pathnão são os únicos utilitários relacionados a arquivos / sistemas de arquivos na biblioteca padrão do Python. O globmódulo é outro módulo útil relacionado ao caminho.

Podemos usar a **glob.glob** função para encontrar arquivos que correspondam a um determinado padrão:

```python
from glob import glob

top_level_csv_files = glob('*.csv')
all_csv_files = glob('**/*.csv', recursive=True)
```

O novo pathlibmódulo inclui também utilitários glob-like.

```python
from pathlib import Path

top_level_csv_files = Path.cwd().glob('*.csv')
all_csv_files = Path.cwd().rglob('*.csv')
```

Depois que você começar a usar pathlib mais, você pode esquecer o módulo glob completamente : você tem toda a funcionalidade glob necessária com os Path objetos.

O **pathlib** simplifica os casos simples
O pathlib módulo torna um número de casos complexos um pouco mais simples, mas também torna alguns dos casos simples ainda mais simples.

Precisa ler todo o texto em um ou mais arquivos?

Você poderia abrir o arquivo, ler seu conteúdo e fechar o arquivo usando um with bloco:

```python
from glob import glob

file_contents = []
for filename in glob('**/*.py', recursive=True):
    with open(filename) as python_file:
        file_contents.append(python_file.read())
```

Ou você pode usar o read_text método em Path objetos e uma compreensão de lista para ler o conteúdo do arquivo em uma nova lista, tudo em uma linha:

```python
from pathlib import Path

file_contents = [
    path.read_text()
    for path in Path.cwd().rglob('*.py')
]
```

## 4.2. E se você precisar gravar em um arquivo?

Você poderia usar o opengerenciador de contexto novamente:

```python
with open('.editorconfig') as config:
    config.write('# config goes here')
```    

Ou você poderia usar o write_text método:

```python
Path('.editorconfig').write_text('# config goes here')
```


Se preferir usar open, seja como gerenciador de contexto ou de outra forma, você poderia usar o open método em seu Path objeto:

```python
from pathlib import Path

path = Path('.editorconfig')
with path.open(mode='wt') as config:
    config.write('# config goes here')
```    

Ou, a partir do Python 3.6, você pode até mesmo passar seu Pathobjeto para a openfunção interna:

```python
from pathlib import Path

path = Path('.editorconfig')
with open(path, mode='wt') as config:
    config.write('# config goes here')
```


Objetos de caminho tornam seu código mais explícito

## 4.3. O que as seguintes 3 variáveis ​​apontam? O que seus valores representam?

person = '{"name": "Trey Hunner", "location": "San Diego"}'
pycon_2019 = "2019-05-01"
home_directory = '/home/trey'

Cada uma dessas variáveis ​​aponta para uma string.

Essas strings representam coisas diferentes: uma é um blob JSON, uma é uma data e uma é um caminho de arquivo.
Estas são representações um pouco mais úteis para esses objetos:

```python
from datetime import date
from pathlib import Path

person = {"name": "Trey Hunner", "location": "San Diego"}
pycon_2019 = date(2019, 5, 1)
home_directory = Path('/home/trey')

```

Os objetos JSON desserializam para dicionários, as datas são representadas nativamente usando datetime.date objetos e os caminhos do sistema de arquivos agora podem ser genericamente representados usando pathlib.Path objetos.

Usando Path objetos torna seu código mais explícito. Se você está tentando representar uma data, você pode usar um date objeto. Se você estiver tentando representar um caminho de arquivo, poderá usar um Path objeto.

Eu não sou um forte defensor da programação orientada a objetos. As classes adicionam outra camada de abstração e as abstrações podem, às vezes, adicionar mais complexidade do que simplicidade. Mas a pathlib.Path classe **é uma abstração útil**. Também está se tornando rapidamente uma abstração universalmente reconhecida.

Graças ao PEP 519 , os objetos de caminho de arquivo estão se tornando o padrão para trabalhar com caminhos. A partir do Python 3.6, o embutido openfunção e as várias funções no os, shutile os.pathmódulos de todo o trabalho adequadamente com pathlib.Pathobjectos. Você pode começar a usar o pathlib hoje sem alterar a maior parte do seu código que funciona com caminhos !

O que está faltando no pathlib?
Embora pathlibseja ótimo, não é abrangente. Definitivamente, faltam alguns recursos que descobri que gostaria que o pathlibmódulo fosse incluído .

A primeira lacuna que notei é a falta de shutilequivalentes nos pathlib.Pathmétodos.

Embora você possa passar Pathobjetos (e objetos semelhantes a caminhos) para as shutilfunções de nível superior para copiar / excluir / mover arquivos e diretórios, não há equivalente a essas funções em Pathobjetos.

Então, para copiar um arquivo, você ainda precisa fazer algo assim:

from pathlib import Path
from shutil import copyfile

source = Path('old_file.txt')
destination = Path('new_file.txt')
copyfile(source, destination)
Também não há pathlibequivalente de os.chdir.

Isso significa que você precisará importar chdirse precisar alterar o diretório de trabalho atual:

from pathlib import Path
from os import chdir

parent = Path('..')
chdir(parent)
A os.walkfunção também não tem pathlibequivalente. Embora você possa fazer suas próprias walkfunções semelhantes, usando pathlibbastante facilmente.

Minha esperança é que os pathlib.Pathobjetos possam eventualmente incluir métodos para algumas dessas operações ausentes. Mas, mesmo com esses recursos ausentes, ainda acho muito mais fácil usar “ pathlibe amigos” do que “ os.pathe amigos” .

Você deve sempre usar o pathlib?
Desde o Python 3.6, os objetos pathlib.Path funcionam em quase todos os lugares em que você já está usando strings de caminho . Então não vejo razão para não usar pathlibse você estiver no Python 3.6 (ou superior).

Se você está em uma versão anterior do Python 3, você sempre pode envolver seu Pathobjeto em uma strchamada para obter uma string quando precisar de uma saída de escape para o string land. É estranho mas funciona:

from os import chdir
from pathlib import Path

chdir(Path('/home/trey'))  # Works on Python 3.6+
chdir(str(Path('/home/trey')))  # Works on earlier versions also
Independentemente de qual versão do Python 3 você está, eu recomendo dar pathlibuma chance.

E se você ainda está preso no Python 2 (o relógio está correndo!), O módulo pathlib2 de terceiros no PyPI é um backport para que você possa usá-lo pathlibem qualquer versão do Python.

Eu acho que usar pathlibmuitas vezes torna meu código mais legível. A maior parte do meu código que funciona com arquivos agora é padronizado pathlibe eu recomendo que você faça o mesmo. Se você puder usar pathlib, você deve .

Se você quiser continuar lendo sobre o pathlib, confira meu artigo de acompanhamento chamado No, o pathlib é ótimo .