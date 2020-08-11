#packaging (not so reliable but knowledge)

# /SoloLearn/
	# LISCENSE.txt
	# README.txt
	# setup.py
	# file/
		# __init__.py #blank file but should be(not necessarily) present in a directory
		# module1.py
		# module2.py
		# anyScript.py

#creating setup file
from distutils.core import setup

setup(
	name='SoloLearn',
	version='0.1dev',
	package=['file',],
	license='MIT',
	long_description=open('README.txt').read(),
)

#then upload to PyPl or use cmd for binary distribution
#source distribution - cmd> direct the setup file> run command python setup.py sdist
#binary distribution - bdist_wininst
#use python setup.py register followed by setup.py sdist upload
#install with python setup.py install

#if the user hasn't installed python yet, try to build script files as executable files for platforms (window,Mac)
#py2exe, PyInstaller, cx_Freeze - window
#py2app, PyInstaller, cx_Freeze - Mac