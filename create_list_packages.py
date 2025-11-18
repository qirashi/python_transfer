import pkg_resources

installed_packages = pkg_resources.working_set
with open('installed_packages.txt', 'w') as file:
    for package in installed_packages:
        file.write(package.key + '\n')
