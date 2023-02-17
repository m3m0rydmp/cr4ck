import platform

def get_python_version():
    # Get the version of Python that is installed on the system
    version = platform.python_version()
    return version

# Test the function
print(get_python_version())

