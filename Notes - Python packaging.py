'''This file is not to be executed. 
It is about Python packaging (subject to change with time).'''

### STRUCTURE OF A PACKAGE
# /SoloLearn/
	# LISCENSE.txt
	# README.txt
	# setup.py
	# file/
		# __init__.py ## blank file but should be(not necessarily) present in a directory
		# module1.py
		# module2.py
		# anyScript.py

### CREATING A SETUP FILE
from distutils.core import setup

setup(
	name = 'SoloLearn',
	version = '0.1dev',
	package = ['file',],
	license = 'MIT',
	long_description = open('README.txt').read(),
)

### NEXT STEPS
# upload to PyPl or use CMD for binary distribution
## source distribution - CMD > direct the setup file > run command python setup.py sdist
## binary distribution - bdist_wininst

# use python setup.py register followed by setup.py sdist upload
# install with python setup.py install
# if the user hasn't installed python yet, try to build script files as executable files for platforms (window,Mac)
## py2exe, PyInstaller, cx_Freeze - window
## py2app, PyInstaller, cx_Freeze - Mac
