import pkg_resources
import os
import subprocess
import requests
import time
import pip
import platform


def is_package_installed(package):
    try:
        pkg_resources.get_distribution(package)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def check_current_version():
    
    # Get the version of Python that is installed on the system
    version = platform.python_version()
    return version

def install_latest_python():
    
    #Use pip to install the latest version of Python
    subprocess.run(["pip", "install", "--upgrade", "python"])
    
def install_package(package):
    pip.main(['install', package])

print("Checking Necessary requirements...")
time.sleep(1)

try:
    package_verify = is_package_installed("platform")
    
    if package_verify is False:
        print("Installing package 'request'.")
        install_package("platform")
        print("Download finished...")
    else:
        pass
    
    print("Checking the Python version in your system...")
    time.sleep(1)
    
    current_version = check_current_version()
    print("Python version is: ",current_version)
        
    if current_version >= '3.9':
        print('The current version of Python is 3.9 or newer')
    else:
        print('The current version of Python is older than 3.9')
        print('Updating Python version...')
        time.sleep(1)
        install_latest_python()
    
    print("Downloading necessary packages...")
    
    install_package("rich")
    install_package("progress")
    
    print("All preparations are done.")

except pkg_resources.DistributionNotFound:
    print("The Python package is not installed in this system.")
