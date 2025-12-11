import subprocess

try:
    subprocess.run('py -m pip install PYQT5')
    subprocess.run('py -m pip install reportlab')
    subprocess.run('py -m pip install email_validator')

except Exception as e:
    print (e)
    input("CHeese")