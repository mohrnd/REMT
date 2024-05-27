import subprocess
import os
from pathlib import Path

username = os.getlogin()
path = Path(fr"C:\Users\{username}\Desktop")
subprocess.Popen(f'explorer "{path}"')
