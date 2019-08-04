from pathlib import Path


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


def main():
    # diretorio = Path('monitor')
    diretorio = Path.cwd()
    print(tree(diretorio))


if __name__ == "__main__":
    main()