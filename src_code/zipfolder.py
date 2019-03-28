import zipfile
import os
import sys
import shutil
from pathlib import Path
import collections
import zipfile
from typing import Union
from typing import List


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
    # Diretorio deste arquivo: Path(__file__).parents[0]
    dir_origem = Path(__file__).parents[0] / Path(str_dirname)
    subdir_01 = dir_origem / 'dir01'
    subdir_02 = dir_origem / 'dir02'
        
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
            print('='*80)
            # Path Absoluto + Nome do Arquivo
            print('Path Absoluto + Nome Arquivo: ' + str(item) )
            # Nome do arquivo
            print('Nome do arquivo: ' + str(item.name))
            # Extensão do Arquivo
            print('Extensão: ' + str(item.suffix))        
            # Path Absoluto (desde a raiz)
            print('Resolve() igual ao primeiro: ' + str(item.resolve()))
            # Path Relativo ao diretorio
            print('relative_to(): ' + str(item.relative_to(Path(__file__).parents[0])))
            # Tamanho do arquivo
            print('Tamanho do Arquivo: ' + str(item.stat().st_size))
            # Armazena Path Relativo como String
            lst_files.append(str(item))
            print('='*80)
        
        if item.is_dir():
            print('DIRETORIO parent: ' + str(item.parent))
            print('DIRETORIO: ' + str(item))
            print('='*80)

    print(' CRIADO O DIRETÓRIO DE EXEMPLO COM SUCESSO! ')
    return lst_files    

def zip_dir(source_dir:str, path_zip_output:str) -> Union[bool,str]:
    """
    Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    :param source_dir (str): diretorio que será compactado
    :param path_zip_output (str): path + zipname de saída
    
    Ex: zip_dir('/home/ubuntu/DirOrigem', '/home/ubuntu/DirDestino/file.zip')
    """
    try:
        base = os.path.basename(path_zip_output)
        name = base.split('.')[0] # no extension
        formato_arq = base.split('.')[1]
        root_dir = os.path.dirname(source_dir)
        base_dir = os.path.basename(source_dir.strip(os.sep))
        shutil.make_archive(name, formato_arq, root_dir=root_dir, base_dir=base_dir)
        shutil.move('%s.%s'%(name,formato_arq), path_zip_output)
        try:
            with zipfile.ZipFile(path_zip_output) as f: 
                print("Arquivo {} gerado com sucesso!".format(path_zip_output))
                return False, "Compressão executada com sucesso!"
        except zipfile.BadZipFile as err_msg:
            return True, err_msg        

    except IOError as err_msg:
        return True, err_msg
    except OSError as err:
        return True, err_msg


def zip_folder(folder_path:str, output_path:str) -> Union[bool,str]:
    """Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    Exemplo:
    zip_folder(r'/home/ubuntu/folder_origem',
               r'/home/ubuntu/folder_saida/saida.zip')
    """
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '/','')
                print("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '/','')
                print("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)
        return False, "Compression successfully!"
    except IOError as err_msg:
        return True, err_msg
    except OSError as err_msg:
        return True, err_msg
    except zipfile.BadZipfile as err_msg:
        return True, err_msg
    finally:
        zip_file.close()

def main():
    """
    OBJETIVO: mostrar o uso do SHUTIL MAKEFILE para compactar uma pasta

    Obs: este script constrói um diretório com subdiretórios e arquivos
    para a execução do teste.

    """
    # Qual diretorio você deseja compactar?
    dir_deste_projeto = Path().cwd()
    print('Diretório deste arquivo um nível acima:')
    print(Path(__file__).parents[1])

    print('Diretório deste arquivo:')
    print(Path(__file__).parents[0])
    
    directory = 'DirOrigem'
    
    # Listando os Paths Relativos + Filenames com PATHLIB
    lst_files = construct_subdirExample(directory)
 
    # Contando quantos arquivo .txt temos no diretório diretório ATUAL DO PROJETO (cwd)
    result = collections.Counter(p.suffix for p in Path.cwd().glob('*.txt'))
    print('A quantidade de arquivos do tipo .txt é: {}'.format(result['.txt']))

    # No diretorio específicado acima
    result = collections.Counter(p.suffix for p in Path(directory).glob('*.dat'))
    print('A quantidade de arquivos do tipo .dat: {}'.format(result['.dat']))      

    # COMPACTANDO O DIRETORIO 'DirOrigem' para o arquivo saida.zip

    # Compactar pasta com SHUTIL.make_archive
    zipname_output = str(Path(__file__).parents[0]) + '/zip_saida.zip' 
    zipname_output2 = str(Path(__file__).parents[0]) + '/zip_saida2.zip' 
    dir_to_compress = str(Path(__file__).parents[0]) + '/DirOrigem' 
    # zip_folder(dir_to_compress, zipname_output)
    error, msg = zip_dir(dir_to_compress, zipname_output2)   


if __name__ == "__main__":
    main()