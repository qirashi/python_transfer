import subprocess

def install_package(package):
    subprocess.call(['pip', 'install', package])

with open('installed_packages.txt', 'r') as file:
    packages = file.readlines()
    for package in packages:
        install_package(package.strip())
