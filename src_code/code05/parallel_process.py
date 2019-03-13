import requests
import json
import sys
import os
from pathlib import Path
import logging
import logging.handlers as handlers

from modules import DevelopmentConfig
from concurrent.futures import ProcessPoolExecutor

""" 
Descompactando arquivo Zip em Paralelo
"""

def main():
    try:

        logger = init_log(Path(__file__) / "description.log")
        r = requests.head(DevelopmentConfig.URL_TESTE, timeout=(5, 14))

        # Security: link is avalible?
        if not r.status_code == 200:
            print("=" * 80)
            print(" Script Interrupted!")
            print(" Url do arquivo do ETA40 do ONS {} não está disponível!".format(DevelopmentConfig.URL_TESTE))
            print("=" * 80)
            logger.info(" Script Interrupted! ")
            logger.info(" Url do arquivo do ETA40 do ONS {} não está disponível!".format(DevelopmentConfig.URL_TESTE))
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
        
# -------------------------------------------------------------
# END MAIN


def init_log(pathFileLogName, maximoBytes=2048000, backupCount=3):
        """
        Inicializa um arquivo para armazenar as saídas do script.

        Ex de uso: logger = init_log("t01_tab_users.log")
        Imprima informações:
        logger.info( "ROW: {1} => User: {1}".format(row,user) )

        Por padrão definimos que os arquivos de Log terão no máximo 2Mb
        e serão num total de 3 arquivos.

        :param maximoBytes: numero máximo de bytes que conterão no aquivo de Log
        :param backupCount: numero máximo de arquivos Log que serão escritos
        :param pathFileLogName: path + nome do arquivo de Log que deseja
        :return: Object logger
        """

        # if (not os.path.isfile(pathFileLogName)):
        #     open(pathFileLogName, 'a').close() # Cria um arquivo vazio

        if not Path(pathFileLogName).is_file():
            Path(pathFileLogName).touch() # Cria um arquivo vazio

        logger = logging.getLogger("mylog")
        logger.setLevel(logging.INFO)
        # Here we define our formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logHandler = handlers.RotatingFileHandler(
            pathFileLogName, maxBytes=maximoBytes, backupCount=2)
        logHandler.setLevel(logging.INFO)
        logger.addHandler(logHandler)
        # Here we set our logHandler's formatter
        logHandler.setFormatter(formatter)
        return logger


if __name__ == "__main__":
    main()