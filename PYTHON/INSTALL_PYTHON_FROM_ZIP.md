# COMO INSTALAR O PYTHON DO ARQUIVO ZIP

https://michlstechblog.info/blog/python-install-python-with-pip-on-windows-by-the-embeddable-zip-file/

Extraia o arquivo .zip para a pasta D:\python3.6.5

d:\> cd /d D:\Python3.6.5
D:\Python3.6.5> python get-pip.py
...
Installing collected packages: pip, setuptools, wheel
Successfully installed pip-10.0.1 setuptools-39.2.0 wheel-0.31.1

Infelizmente na configuração padrão você não pode carregar nenhum módulo instalado pelo pip, pip em si também. Porque a variável sys.path apenas contém o arquivo Python Zip e o caminho para o diretório python onde o executável python está localizado.

```python
>>> import sys
>>> print(sys.path)
['D:\\Python3.6.5\\python36.zip', 'D:\\Python3.6.5']
>>> import pip
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pip'
```

Qualquer tentativa de expandir a variável definindo uma variável PYTHONPATH será ignorada . A causa raiz é que o pacote de instalação do arquivo zip embutido contém um arquivo python36._pth que substitui todas as outras possibilidades para definir a variável sys.path. sys.path contém todos os diretórios onde o python procura por módulos.

Para definir a variável sys.path, abra o arquivo _pth e adicione os seguintes trechos no e do arquivo. Substitua "D: \ Python3.6.5" pelo seu diretório de instalação.


```
D:\Python3.6.5
D:\Python3.6.5\DLLs
D:\Python3.6.5\lib
D:\Python3.6.5\lib\plat-win
D:\Python3.6.5\lib\site-packages
```

Ou renomeie o arquivo python36._pth

D:\Python3.6.5> ren python36._pth python36._pth.save

e defina a variável de ambiente PYTHONPATH para o usuário atual.

setx PYTHONPATH "D:\Python3.6.5;D:\Python3.6.5\DLLs;D:\Python3.6.5\lib;D:\Python3.6.5\lib\plat-win;D:\Python3.6.5\lib\site-packages"

