import subprocess as sbp
import pip
import os

pkgs = eval(str(sbp.run("pip3 list -o --format=json", shell=True,
                         stdout=sbp.PIPE).stdout, encoding='utf-8'))
for pkg in pkgs:
    sbp.run("pip3 install --upgrade " + pkg['name'], shell=True)

os.system('python -m pip install --upgrade pip')