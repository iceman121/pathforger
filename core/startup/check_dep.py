import os
import subprocess
import pkg_resources

REQ = 'assets/requirements.txt'


def iter_dep():
    # Get dependencies
    with open(REQ, 'r') as f:
        dep_list = f.readlines()
        f.close()
    dep_list = [i.replace('\n', '') for i in dep_list]

    # Get list of installed packages
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(['{}=={}'.format(i.key, i.version) for i in installed_packages])

    # Run package installation if any package is not installed
    for pkg in dep_list:
        if pkg not in installed_packages_list:
            subprocess.call('scripts\install_dep.bat')  # noqa
            break
    os.system('cls')


def install_dep():
    iter_dep()


install_dep()
