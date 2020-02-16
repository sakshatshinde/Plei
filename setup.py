import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('app.py', base=base)
]

setup(name='Plei',
      version='0.1',
      description='A bloat free game launcher',
      executables=executables
      )