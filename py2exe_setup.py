# -*- coding: utf-8 -*-
"""
      _             _                              _                   
     | |           | |                            | |                  
  ___| |_ __ _  ___| | __  ___ _ __ ___   __ _ ___| |__   ___ _ __ ___ 
 / __| __/ _` |/ __| |/ / / __| '_ ` _ \ / _` / __| '_ \ / _ \ '__/ __|
 \__ \ || (_| | (__|   <  \__ \ | | | | | (_| \__ \ | | |  __/ |  \__ \
 |___/\__\__,_|\___|_|\_\ |___/_| |_| |_|\__,_|___/_| |_|\___|_|  |___/

@author: Andrea Simeoni 12 ott 2017   
https://github.com/insanediv/python-screenshot-easy-run/blob/master/py2exe_setup.py
"""
from distutils.core import setup
import shutil
import py2exe

import os
dataFiles = []

APP_NAME = "pyscreenshots"
VERSION = "1.0.0.000"


def list_dir(dirname, destdir):
    result = []
    for file in os.listdir(dirname):
        f1 = os.path.join(file, dirname)
        f2 = destdir, [f1]
        result.append(f2)
    return result


class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)


lib_files = list_dir('lib', 'lib')
app_files = list_dir('app', 'app')

target32 = Target(
    script="src\\setup32.py",
    version=VERSION,
    company_name="fsociety001",
    name=APP_NAME,
)

target64 = Target(
    script="src\\setup64.py",
    version=VERSION,
    company_name="fsociety001",
    name=APP_NAME,
)

setup(
    author='Andrea Simeoni',
    author_email='andreasimeoni84@reply.it',
    description = 'Take screenshots with right mouse button',
    console = [target32, target64],
)

os.system('Xcopy /E /I app dist\\app')
os.system('Xcopy /E /I lib dist\\lib')

# Create output dir
output_dir = '%s-%s' % (APP_NAME, VERSION)
os.system('mkdir %s' % output_dir)
os.system('Xcopy /E /I dist %s' % output_dir)
shutil.make_archive(output_dir, 'zip', output_dir)

# clean
os.system('rmdir build /s /q')
os.system('rmdir dist /s /q')
os.system('rmdir %s /s /q' % output_dir)
