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

Aqui estão alguns exemplos que eu notei usando **pathlib** em poucos dias:

## 1.5. Trabalhando com Pastas (Diretórios)

```
from pathlib import Path
```

## 1.6. Verificando se o diretório existe

Path('docs').exists()
False

## 1.7. Criando o Diretório

Path('docs').mkdir()

## 1.8. Verificando se é um diretório
>>> Path('docs').is_dir()
True

## 1.9. Listando todos _os_ arquivos dentro de um diretório
>>> Path('docs').glob('*.md')
<generator object Path.glob at 0x1128ee258>

## 1.10. Uma vez que a saída não é óbvia: 

>>> [item for item in Path('docs').glob('*.md')]
[PosixPath('docs/README.md')]

## 1.11. Trabalhando com Arquivos

>>> Path('docs', 'README.md').is_file()
True

>>> Path('docs').joinpath('README.md')

## 1.12. Abrindo um arquivo para Leitura

>>> Path('README.md').open('r').read()

## 1.13. Escrevendo para um Arquivo

>>> Path('README.md').write_text('Read the Docs!')

## 1.14. Lendo o conteúdo do arquivo

>>> Path('README.md').read_text()
'Read the Docs!'
What about Python 2?
Even though pathlib is built into Python 3, there is a Python 2.7 backport for anyone who can’t switch yet.


# 2. APLICAÇÕES

## 2.1. Como construir a Árvore de Diretórios e Arquivos com PATHLIB

Importações necessárias:

```python
from pathlib import Path
```

Modo de uso:

```bash
    diretorio = Path('monitor')
    print(tree(diretorio))
```

Este método construirá a árvore de diretório igual a do comando **tree** do linux:





```python
def tree(directoryPathlib):
    """
        Parâmetro:

        params directoryPathlib: (pathlib.Path())
        
        O próximo exemplo define uma função, tree() que imprimirá uma               árvore visual representando a hierarquia de arquivos, com raiz em           um determinado diretório. Aqui, queremos listar subdiretórios               também, então usamos o .rglob() método.

        OBSERVE que precisamos saber a que distância do diretório raiz um           arquivo está localizado. 

        Para fazer isso, primeiro usamos .relative_to() para representar um         caminho relativo ao diretório raiz. Em seguida, contamos o número           de diretórios (usando a .parts propriedade) na representação. 
        Quando executado, essa função cria uma árvore visual como a                 seguinte:

        + / home / mpi / realpython 
            + diretório_1 
                + arquivo_a.md 
            + diretório_2 
                + arquivo_a.md 
                + arquivo_b.pdf 
                + arquivo_c.py 
            + arquivo_1.txt 
            + arquivo_2.txt        

    """
    print(f'+ {directoryPathlib}')
    for path in sorted(directoryPathlib.rglob('*')):
        depth = len(path.relative_to(directoryPathlib).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

```


## 2.2. RESUMO

https://stackabuse.com/introduction-to-the-python-pathlib-module/

Usando o Pathlib, os.getcwd () se torna Path.cwd () e o operador '/' é usado para unir caminhos e usado no lugar de os.path.join. Usando o módulo Pathlib, as coisas podem ser feitas de maneira mais simples usando operadores e chamadas de método.

A seguir estão os métodos comumente usados ​​e seu uso:

* Path.cwd(): Objeto de caminho de retorno representando o diretório de * trabalho atual
* Path.home(): Objeto de caminho de retorno representando o diretório inicial
* Path.stat(): informações de retorno sobre o caminho
* Path.chmod(): alterar o modo de arquivo e permissões
* Path.glob(pattern): Glob o padrão dado no diretório que é representado pelo * caminho, produzindo arquivos correspondentes de qualquer tipo
* Path.mkdir(): para criar um novo diretório no caminho fornecido
* Path.open(): Para abrir o arquivo criado pelo caminho
* Path.rename(): Renomear um arquivo ou diretório para o destino determinado
* Path.rmdir(): Remover o diretório vazio
* Path.unlink(): Remover o arquivo ou link simbólico

Gerando Caminhos de Plataforma Cruzada

Caminhos usam diferentes convenções em diferentes sistemas operacionais. O Windows usa uma barra invertida entre nomes de pastas, enquanto todos os outros sistemas operacionais populares usam barra entre os nomes das pastas. Se você quiser que seu código python funcione, independentemente do SO subjacente, você precisará lidar com as diferentes convenções específicas da plataforma subjacente. O módulo Pathlib facilita o trabalho com caminhos de arquivos. No Pathlib, você pode simplesmente passar um caminho ou um nome de arquivo para o Path()objeto usando a barra, independentemente do sistema operacional. O Pathlib cuida do resto.

```python
pathlib.Path.home() / 'python' / 'samples' / 'test_me.py'  
```

O Path() objeto converterá / para o tipo de barra, para o sistema operacional subjacente. O pathlib.Path pode representar o caminho do Windows ou Posix. Assim, o Pathlib resolve muitos bugs interfuncionais, ao manipular caminhos facilmente.

## 2.3. Obtendo informações sobre o caminho

Ao lidar com caminhos, estamos interessados ​​em encontrar o diretório pai de um arquivo / pasta ou nos links simbólicos a seguir. A classe de caminho tem vários métodos convenientes para fazer isso, já que diferentes partes de um caminho estão disponíveis como propriedades que incluem o seguinte:

drive: uma string que representa o nome da unidade. Por exemplo, PureWindowsPath('c:/Program Files/CSV').driveretorna "C:"
parts: retorna uma tupla que fornece acesso aos componentes do caminho
name: o componente de caminho sem nenhum diretório
parent: seqüência fornecendo acesso aos ancestrais lógicos do caminho
stem: componente do caminho final sem seu sufixo
suffix: a extensão do arquivo do componente final
anchor: a parte de um caminho antes do diretório. /é usado para criar caminhos filhos e imita o comportamento de os.path.join.
joinpath: combina o caminho com os argumentos fornecidos
match(pattern): retorna verdadeiro / falso, com base na correspondência do caminho com o padrão de estilo glob fornecido
No caminho "/home/projects/stackabuse/python/sample.md":

* **path**: - retorna PosixPath ('/home/projects/stackabuse/python/sample.md')
* **path.parts**: - retorna ('/', 'home', 'projects', 'stackabuse', 'python')
* **path.name**: - retorna 'sample.md'
* **path.stem**: - retorna 'amostra'
* **path.suffix**: - retorna '.md'
* **path.parent**: - retorna PosixPath ('/home/projects/stackabuse/python')
* **path.parent.parent**: - retorna PosixPath ('/home/projects/stackabuse')
* **path.match('*.md')**: retorna verdadeiro
* **PurePosixPath('/python').joinpath('edited_version')**: returns ('home/ * projetos/stackabuse/python/edited_version



# 3. ARTIGO II


## 3.1. os.path é desajeitado!

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

## 3.2. COMO FICA COM PATHLIB?

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')
```

* Path(__file__).resolve() apresenta o caminho do arquivo em questão. 
* Path(__file__).resolve().parent.parent sobe 2 níveis de diretórios


Motivos para deixar de usar o **os.path**

O os.path módulo requer aninhamento de funções, mas a classe pathlib dos módulos Path nos permite encadear métodos e atributos em Path objetos para obter uma representação de caminho equivalente.

Eu sei o que você está pensando: espere que esses Path objetos não sejam a mesma coisa: eles são objetos, não cordas de caminho! Vou abordar isso mais tarde (dica: isso pode ser usado de forma intercambiável com strings de caminho).

O módulo **os** está lotado
O os.path módulo clássico do Python é apenas para trabalhar com caminhos. Uma vez que você queira realmente fazer algo com um caminho (por exemplo, criar um diretório), você precisará procurar outro módulo Python, geralmente o osmódulo.

O **os** módulo tem muitas utilidades para trabalhar com arquivos e diretórios: mkdir, getcwd, chmod, stat, remove, rename, e rmdir. Além disso chdir, link, walk, listdir, makedirs, renames, removedirs, unlink(a mesma que remove), e symlink. E um monte de outras coisas que não está relacionado com os sistemas de arquivos em tudo: fork, getenv, putenv, environ, getlogin, e system. Mais dezenas de coisas que não mencionei neste parágrafo.

O **os** módulo do Python faz um pouco de tudo; é uma espécie de gaveta de lixo para coisas relacionadas ao sistema . Há muitas coisas bonitas no osmódulo, mas pode ser difícil encontrar o que você está procurando às vezes: se você está procurando por coisas relacionadas ao caminho ou relacionadas ao sistema de arquivos no osmódulo, você precisará fazer uma pouco de cavar.

O **pathlib** módulo substitui muitos desses **os** utilitários relacionados ao sistema de arquivos por métodos no **Path** objeto.

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

Observe que o pathlib código coloca o caminho primeiro devido ao encadeamento do método!

Como o Zen of Python diz, “namespaces são uma grande ideia, vamos fazer mais daquelas”. O **os** módulo é um namespace muito grande com um monte de coisas nele. A classe **pathlib.Path** é um namespace muito menor e mais específico que o módulo **os**. Além disso, os métodos neste Path namespace retornam Path objetos, o que permite o encadeamento de métodos em vez de chamadas de função stringiful aninhadas.

## 3.3. Não se esqueça do módulo glob!

Os módulos ose os.path não são os únicos utilitários relacionados a arquivos/sistemas de arquivos na biblioteca padrão do Python. O **glob** módulo é outro módulo útil relacionado ao caminho.

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

## 3.4. E se você precisar gravar em um arquivo?

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

## 3.5. O que as seguintes 3 variáveis ​​apontam? O que seus valores representam?

person = '{"name": "Trey Hunner", "location": "San Diego"}'
pycon_2019 = "2019-05-01"
home_directory = '/home/trey'

Cada uma dessas variáveis ​​aponta para uma string.

Essas strings representam coisas diferentes: 
    > uma é um blob JSON, uma é uma data e uma é um caminho de arquivo.

Estas são representações um pouco mais úteis para esses objetos:

```python
from datetime import date
from pathlib import Path

person = {"name": "Trey Hunner", "location": "San Diego"}
pycon_2019 = date(2019, 5, 1)
home_directory = Path('/home/trey')
```

Os objetos JSON desserializam para dicionários, as datas são representadas nativamente usando datetime.date objetos e os caminhos do sistema de arquivos agora podem ser genericamente representados usando pathlib.Path objetos.

Usando Path objetos torna seu código mais explícito. Se você está tentando representar uma data, você pode usar um date objeto. 
Se você estiver tentando representar um caminho de arquivo, poderá usar um Path objeto.

Eu não sou um forte defensor da programação orientada a objetos. As classes adicionam outra camada de abstração e as abstrações podem, às vezes, adicionar mais complexidade do que simplicidade. Mas a pathlib.Path classe **é uma abstração útil**. Também está se tornando rapidamente uma abstração universalmente reconhecida.

Graças ao **PEP 519**, os objetos de caminho de arquivo estão se tornando o padrão para trabalhar com caminhos. A partir do Python 3.6, o embutido a função **open** e as várias funções no **os**, **shutil** e os.path módulos de todo o trabalho adequadamente com pathlib.Path objectos. Você pode começar a usar o pathlib hoje sem alterar a maior parte do seu código que funciona com caminhos!

## 3.6. O que está faltando no pathlib?

Embora pathlib seja ótimo, **não é abrangente**. Definitivamente, faltam alguns recursos que descobri que gostaria que o pathlib módulo fosse incluído.

A primeira lacuna que notei é a falta de shutil equivalentes nos pathlib.Path métodos.

Embora você possa passar Path objetos (e objetos semelhantes a caminhos) para as shutil funções de nível superior para copiar / excluir / mover arquivos e diretórios, não há equivalente a essas funções em Path objetos.

## 3.7. Então, para copiar um arquivo, você ainda precisa fazer algo assim:

```python
from pathlib import Path
from shutil import copyfile

source = Path('old_file.txt')
destination = Path('new_file.txt')
copyfile(source, destination)
```

Também não há pathlib equivalente de os.chdir.

Isso significa que você precisará importar chdir se precisar alterar o diretório de trabalho atual:

```python
from pathlib import Path
import os

parent = Path('..')
os.chdir(parent)
```


A os.walk função também não tem pathlib equivalente. Embora você possa fazer suas próprias walk funções semelhantes, usando pathlib bastante facilmente.
Minha esperança é que os pathlib.Path objetos possam eventualmente incluir métodos para algumas dessas operações ausentes. Mas, mesmo com esses recursos ausentes, ainda acho muito mais fácil usar “pathlib e amigos” do que “os.path e amigos” .

## 3.8. Você deve sempre usar o pathlib?

Desde o Python 3.6, os objetos pathlib.Path funcionam em quase todos os lugares em que você já está usando strings de caminho . Então não vejo razão para não usar pathlibse você estiver no Python 3.6 (ou superior).

Se você está em uma versão anterior do Python 3, você sempre pode envolver seu Path objeto em uma str chamada para obter uma string quando precisar de uma saída de escape para o string land. É estranho mas funciona:

```python
from os import chdir
from pathlib import Path

chdir(Path('/home/trey'))  # Works on Python 3.6+
chdir(str(Path('/home/trey')))  # Works on earlier python versions also
```

Independentemente de qual versão do Python 3 você está, eu recomendo dar pathlib uma chance.

E se você ainda está preso no Python 2 (o relógio está correndo!), O módulo pathlib2 de terceiros no PyPI é um backport para que você possa usá-lo pathlib em qualquer versão do Python.

Eu acho que usar pathlib muitas vezes torna meu código mais legível. A maior parte do meu código que funciona com arquivos agora é padronizado pathlib e eu recomendo que você faça o mesmo. Se você puder usar pathlib, você deve .

