 
import sys
from cx_Freeze import setup, Executable

BASE = None

if sys.platform == "win32":
    BASE = "Win32GUI"

build_exe_options = {
    # Packages to include
    'includes': [],
    # Files to include
    'include_files': []
}

setup(name="PyDoor",
      version="1.1",
      description="Remote Administration Tool",
      options={'build_exe': build_exe_options},
      executables=[Executable("client.py", base=BASE)])

# python setup.py build