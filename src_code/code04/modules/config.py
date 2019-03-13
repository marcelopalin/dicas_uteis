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
  
  
    URL_TESTE = 'https://pops.ons.org.br/ons.pop.federation/?ReturnUrl=https%3a%2f%2fagentes.ons.org.br%2foperacao%2fpop%2feta%2feta_brasil_01.aspx'
      
    if (get_platform() == 'windows'):

        DIR_BASE = os.path.dirname(os.getcwd()) + "/"
        DIR_BASE_PROJ_LOCAL = str(DIR_BASE) + '/cron_monitor/'

    if (Utils.get_platform() == 'linux'):

        # Usando PathLib
        DIR_BASE = Utils.get_project_root()
        DIR_BASE_PROJ_LOCAL = str(DIR_BASE) + '/cron_monitor/'

        # ATENÇÃO: os diretórios são dividos para alteração de permissões e para sincronismo

        # ALTERAÇÃO DE PERMISSÕES
        DIR_ETA40_NEXTCLOUD_FULL = '/home/ampere/nextcloud-data/' + str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/ETA40'
        DIR_GEFS_NEXTCLOUD_FULL = '/home/ampere/nextcloud-data/' + str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/GEFS'
        DIR_PREVC_NEXTCLOUD_FULL = '/home/ampere/nextcloud-data/' + str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/PREVC'
        DIR_CFSV2_MEMBROS_NEXTCLOUD_FULL = '/home/ampere/nextcloud-data/' + str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/CFSv2/membros'

        # SINCRONISMO DE ARQUIVOS
        DIR_ETA40_NEXTCLOUD_TO_SYNC = str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/ETA40'
        DIR_GEFS_NEXTCLOUD_TO_SYNC = str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/GEFS'
        DIR_PREVC_NEXTCLOUD_TO_SYNC = str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/PREVC'
        DIR_CFSV2_MEMBROS_NEXTCLOUD_TO_SYNC = str(USER_NEXTCLOUD) + '/files/Planejamento/HIDRAULICO/_diaria/CFSv2/membros'

        # DIRETORIOS EXECUTAVEIS
        DIR_EXE_WGRIB2 = '/opt/grib2/wgrib2/wgrib2'
        DIR_EXE_GRADS = '/opt/opengrads/grads'
        DIR_EXE_OPENGRADS = '/opt/opengrads/opengrads'
        DIR_EXE_OCC_NEXTCLOUD = '/home/ampere/nextcloud/occ'

  
class DevelopmentConfig(Config):
    DEBUG = True
    PATH_ETA40 = os.getcwd() + '/ETA40'
    PATH_ETA40 = os.getcwd() + '/ETA40'


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'database-uri-for-dev'


def get_platform():
    """
    Objetivo: padronizar a descoberta dos sistema operacional
    em apenas 3 respostas: windows, linux e macosx.
    Muito utilizado para trabalhar com diretórios.

    Imports: sys
    """
    platforms = {
        'linux1': 'linux',
        'linux2': 'linux',
        'darwin': 'macosx',
        'win32': 'windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]