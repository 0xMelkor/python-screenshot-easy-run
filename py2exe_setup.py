# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

import os
dataFiles = []


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
    version="1.0.0.000",
    company_name="fsociety001",
    name='pyscreenshots',
)

target64 = Target(
    script="src\\setup64.py",
    version="1.0.0.000",
    company_name="fsociety001",
    name='pyscreenshots',
)

setup(
    author='Andrea Simeoni',
    author_email='andreasimeoni84@reply.it',
    description = 'Take screenshots with right mouse button',
    console = [target32, target64]
)

# os.system('Xcopy /E /I app dist\\app')
# os.system('Xcopy /E /I lib dist\\lib')
os.system('mklink setup32.exe dist\\setup32.exe')
os.system('mklink setup64.exe dist\\setup64.exe')
os.system('rmdir build /s /q')
