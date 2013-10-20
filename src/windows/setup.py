#build with: pythonpath setup.py bdist --format=msi

import sys
from cx_Freeze import setup, Executable

setup(
    name = "Lockwatcher",
    version = "0.1",
    description = "An anti-tampering monitor",
    executables = [Executable("lockwatcher-gui.py", base = "Win32GUI",icon='favicon.ico'),
                   Executable('serviceconfig.py', base='Win32Service',targetName='LockWatcherSvc.exe')],
    data_files=[('', ['favicon.ico']),
                ('', ['btscanner.exe','chastrigger.exe','roomtrigger.exe','install-interception.exe','pythonservice.exe']),
                ('', ['roomcam.png','chascam.png','camid.png']),
                ('', ['cygwin1.dll','interception.dll'])
                ],
    options = {'build_exe': {'includes': ['devdetect']}},
    
    
    )