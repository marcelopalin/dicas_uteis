# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
#  Configurações de Projeto
# -------------------------------------------------------------------------------
import os
import sys
try:
    from pathlib import Path
except ImportError as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'lineno': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__
    }
    print("#" * 80)
    print("# Descrição: " + str(e))
    print(traceback_details)
    print("#" * 80)
    sys.exit()

class Config:
  
    if (sys.platform == 'linux'):
        # Retorna um diretorio referente ao 
        DIR_BASE = Path(__file__)._parent

  
class DevelopmentConfig(Config):
    URL_TESTE = 'https://www.peterbe.com/unzip-in-parallel/symbols-2017-11-27T14_15_30.zip'

class ProductionConfig(Config):
    URL_TESTE = 'https://www.peterbe.com/unzip-in-parallel/symbols-2017-11-27T14_15_30.zip'


