import zipfile
import os
import sys
from zipfile import ZipFile
from pathlib import Path

# https://indianpythonista.wordpress.com/2016/12/21/working-with-zip-files-in-python/
# Aqui, precisaremos rastrear todo o diretório e seus subdiretórios para obter uma lista de todos os caminhos de arquivo antes de gravá-los em um arquivo zip. 
# O programa a seguir faz isso rastreando o diretório a ser compactado:

def get_all_file_paths(directory):
     # initializing empty file paths list
    file_paths = []
     # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    # returning all file paths
    return file_paths   



def construct_subdirExample(str_dirname):
    """

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

    return lst_files    

def main():
    
    # Qual diretorio você deseja compactar?
    dir_deste_projeto = Path().cwd()
    
    directory = 'DirOrigem'
    
    # Listando os Paths Relativos + Filenames com PATHLIB
    lst_files = construct_subdirExample(directory)
 
    # Listando os Paths Relativos + Filenames com os.walk
    file_paths = get_all_file_paths(directory)
 
    # writing files to a zipfile
    zip01 = Path().cwd() / 'DirOrigem_01.zip'
    print('='*40)
    print('Gerando o arquivo: {}'.format(zip01))
    print('='*40)
    with ZipFile(zip01,'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
    
    print('Diretório {} compactado em {} !'.format(directory, 'DirOrigem_01.zip'))   

    print('='*40)
    print('Gerando o arquivo: {}'.format(zip01))
    print('='*40)
    with ZipFile('DirOrigem_02.zip','w') as zip:
        # writing each file one by one
        for file in lst_files:
            zip.write(file)       

    print('Diretório {} compactado em {} !'.format(directory, 'DirOrigem_02'))        
 
    
      


if __name__ == "__main__":
    main()