import sys
import os
from cx_Freeze import setup, Executable

# Definir oque deve ser incluido na pasta
# saida de arquivos

configuracao = Executable(
	script='app.py')

# configurar o executavel

setup(
name = 'Automatizador de login',
options = {'build_exe':{'include_msvcr': True}},
executables = [configuracao])