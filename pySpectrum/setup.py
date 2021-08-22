import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("pySpectrum.py",
                                    base=base,
                                    icon="icons/Spectruino.ico")]

cx_Freeze.setup(
    name="pySpectrum",
    options={"build_exe": {"packages": ["serial", "pyqtgraph", "numpy", "PyQt5", "PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets", "pickle"],
                           "include_files": ["icons/",
                                             "icons",
                                             "wavelen2rgb.py"],
                           "includes": ["atexit", "PyQt5.QtNetwork"],
                           "excludes": ["tkinter", "matplotlib"]
                           }
             },
    version="1.3",
    author="Davide Ruzza",
    description="Spectrum analyzer of TCD1304",
    executables=executables
    )