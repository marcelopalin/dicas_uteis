# SINCRONIZANDO DUAS PASTAS (EXCLUINDO DIRS E ARQS DA SINCRONIZAÇÃO)


É eficiente copiar e sincronizar arquivos para ou a partir de um computador remoto.
Suporta cópia de links, propriedades de arquivos como usuário, grupos e permissões.
É mais rápido do que o scp ( Secure Copy ), porque rsync usa protocolo de atualização remota que permite transferir apenas as diferenças entre dois conjuntos de arquivos. Na primeira vez, ele copia todo o conteúdo de um arquivo ou um diretório de origem para o destino, mas a partir da próxima vez, ele copia apenas os blocos alterados e bytes para o destino.
Rsync consome menos banda , uma vez que usa o método de compressão e descompressão durante o envio e recebimento de dados em ambas as extremidades.


```bash
   rsync -avzhe ssh --progress --exclude-from 'lista_exclusao.txt' /home/ubuntu/meteorologia/outputs/CFSv2/membros/2019062600.01 exclusivo:/home/ampere/imagens-previsao/cfsv2/membros/2019/06/26/
   rsync -avzhe ssh --progress --exclude-from 'lista_exclusao.txt' /home/ubuntu/meteorologia/outputs/CFSv2/membros/2019062606.01 exclusivo:/home/ampere/imagens-previsao/cfsv2/membros/2019/06/26/
   rsync -avzhe ssh --progress --exclude-from 'lista_exclusao.txt' /home/ubuntu/meteorologia/outputs/CFSv2/membros/2019062612.01 exclusivo:/home/ampere/imagens-previsao/cfsv2/membros/2019/06/26/
   rsync -avzhe ssh --progress --exclude-from 'lista_exclusao.txt' /home/ubuntu/meteorologia/outputs/CFSv2/membros/2019062618.01 exclusivo:/home/ampere/imagens-previsao/cfsv2/membros/2019/06/26/
```


Onde a lista de exclusão contém as pastas e arquivos que estão na ORIGEM e que não serão SINCRONIZADOS.
Conteúdo do arquivo **lista_exclusao.txt**:

```bash
monthly
src
weekly
*.grb2
*.nc
```

