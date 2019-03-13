# -*- coding: utf-8 -*-
"""
    Importe aqui todos os modulos necessários para o seu projeto.
"""
import sys

try:
    from .config import DevelopmentConfig
except ImportError as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("#" * 80)
    print("# Descrição: " + str(e))
    print('# Nome do Arquivo: ' + str(exc_traceback.tb_frame.f_code.co_filename) + '\n' +
          '# Linha: ' + str(exc_traceback.tb_lineno) + '\n' +
          '# Code Name: ' + str(exc_traceback.tb_frame.f_code.co_name) + '\n' +
          '# Tipo: ' + str(exc_type.__name__))
    print("#" * 80)
    sys.exit()