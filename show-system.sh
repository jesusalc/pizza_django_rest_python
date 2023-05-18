#!from pathlib import Path
import os
import socket
import platform

print(socket.gethostname())
print( platform.uname() )
print( platform.uname().system )

print( repr( os.sys.argv ) )
print( repr( os.sys.argv ) )
print( repr( os.getenv("PWD") ) )
print( repr( os.getenv("HOME") ) )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print( repr( os.getenv("BASE_DIR") ) )
	