import sys
import subprocess
# implement pip as a subprocess:
def pip_install_pythonfile():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','selenium'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','webdriver-manager'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pytest'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'jproperties'])