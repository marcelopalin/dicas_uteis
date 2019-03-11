# ZIPFILE em PYTHON


Objetivo:

Compactar o subdiretório onde está meu script chamado **DirOrigem** para um arquivo chamado DirOrigem.zip!


```python
import zipfile
import os
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

def main():
    # path to folder which needs to be zipped
    directory = './DirOrigem'
 
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
 
    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
 
    # writing files to a zipfile
    with ZipFile('DirOrigem.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
 
    print('All files zipped successfully!')     


if __name__ == "__main__":
    main()
```