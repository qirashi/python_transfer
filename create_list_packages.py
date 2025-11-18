from importlib.metadata import distributions

installed_packages = [dist.metadata["Name"] for dist in distributions()]

with open('save_packages.txt', 'w') as file:
    for package_name in installed_packages:
        file.write(package_name + '\n')