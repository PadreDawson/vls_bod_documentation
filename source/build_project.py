import os


os.system('.\source\make.bat clean')
os.system('.\source\make.bat html')
# os.system('sphinx-build -b pdf source pdf')
os.system('xcopy .\source\_build\html\* .\docs /e /y')