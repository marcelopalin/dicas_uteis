# Enviando E-mail com Python 3

```python

#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      
#
# Created:     
# Copyright:   
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# encoding: utf-8
"""
python_3_email_with_attachment.py
Created by Robert Dempsey on 12/6/14.
Copyright (c) 2014 Robert Dempsey. Use at your own peril.

This script works with Python 3.x

NOTE: replace values in ALL CAPS with your own values
"""
import sys
import os
import string
from string import ascii_lowercase
import re
import calendar
import datetime
import locale
from locale import setlocale, LC_ALL
import math
import operator
import csv
from types import *
import shutil, errno
import getpass
import time
from pathlib import Path

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def main():
    sender = 'myemail@gmail.com'
    gmail_password = 'MY_PASS_FROM_GMAIL'
    recipients = ['user01_to_receive@gmail.com,user02_to_receive@gmail.com']

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Enviando Email por Python 3'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    # Arquivo de anexo - vamos supor que o arquivo esteja no mesmo diretório que este script
    anexo = Path('anexo.pdf').resolve() # sera o mesmo que /home/user/myproj/anexo.pdf
    attachments = [anexo]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email foi enviado!!")
    except:
        print("Não foi possível enviar o e-mail!. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    main()


```