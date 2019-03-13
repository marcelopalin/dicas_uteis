import zipfile
import os
import sys
from zipfile import ZipFile
from pathlib import Path
import collections



def construct_subdirExample(str_dirname):
    """
        Método auxiliar para utilizarmos nosso exemplo.
        Constrói um conjunto de Diretórios e arquivos
        para serem testados.

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
    
    """
    dir_origem = Path('.') / Path(str_dirname)
    subdir_01 = Path(str_dirname) / 'dir01'
    subdir_02 = Path(str_dirname) / 'dir02'
        
    # Vefifica se o diretorio existe
    if not dir_origem.is_dir():
        dir_origem.mkdir(parents=True, exist_ok=True)

    if not subdir_01.is_dir():
        subdir_01.mkdir(parents=True, exist_ok=True)

    if not subdir_02.is_dir():
        subdir_02.mkdir(parents=True, exist_ok=True)

    path_file = Path(subdir_01, 'f001.txt')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_01, 'f002.txt')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_01, 'f003.txt')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_01, 'arq01.dat')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_01, 'arq02.dat')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_02, 'a001.dat')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_02, 'a002.dat')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch() 

    path_file = Path(subdir_02, 'f.zip')
    if not path_file.is_file():
        path_file.parent.mkdir(parents=True, exist_ok=True)
        path_file.touch()   

    lst_files = []

    # Loop pelos diretorios e arquivos
    for item in dir_origem.glob('**/*'):
        if item.is_file():
            # Path Relativo + Nome do Arquivo
            print(item) 
            # Nome do arquivo
            print(item.name)
            # Extensão do Arquivo
            print(item.suffix)            
            # Path Absoluto (desde a raiz)
            print(item.resolve()) 
            # Tamanho do arquivo
            print(item.stat().st_size)
            # Armazena Path Relativo como String
            lst_files.append(str(item))
        
        if item.is_dir():
            print(item.parent)

    print(' CRIADO O DIRETÓRIO DE EXEMPLO COM SUCESSO! ')
    return lst_files    

def main():
    """
    OBJETIVO: mostrar o uso do PATHLIB para lidar com diretórios e arquivos.


    """
    # Qual diretorio você deseja compactar?
    dir_deste_projeto = Path().cwd()
    
    directory = 'DirOrigem'
    
    # Listando os Paths Relativos + Filenames com PATHLIB
    lst_files = construct_subdirExample(directory)
 
    # Contando quantos arquivo .txt temos no diretório diretório ATUAL DO PROJETO (cwd)
    result = collections.Counter(p.suffix for p in Path.cwd().glob('*.txt'))
    print('A quantidade de arquivos do tipo .txt é: {}'.format(result['.txt']))

    # No diretorio específicado acima
    result = collections.Counter(p.suffix for p in Path(directory).glob('*.dat'))
    print('A quantidade de arquivos do tipo .dat: {}'.format(result['.dat']))      
        
      


if __name__ == "__main__":
    main()