import platform
import subprocess

import sys
import subprocess

def getPackageVersion(packageName):
    # Returns the version of the package, or returns None if not installed

    # Get installed packages with their versions
    package_versions = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    package_versions = package_versions.decode('utf-8')
    
    for package in package_versions.splitlines():
        name, version = package.split('==')
        if name == packageName:
            return version
        
    return None

def install(packageName):
    # Installs a package, checking and printing the results

    # <current_python> -m pip install package
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', packageName])

    # Check that the package is installed
    packageVersion = getPackageVersion(packageName)
    if packageVersion is None:
        print(f'Failed to install {packageName}. Please capture the output in the terminaland send to an instructor.')
    else:
        print(f'Success: {packageName} is installed (version {packageVersion})')

# result = platform.system()
# print(type(result))
# print(result)

# Check if the OS is a version of Mac OS and then check if brew is installed
if platform.system() == "Darwin":
    print("It looks like your are running Mac OSX...")
    print()
    try:
        print("Checking if brew is installed...")
        output = subprocess.check_output(["brew", "--version"], text=True)
        print(f"Succesfully found brew, version {output}")
    except FileNotFoundError:
        print("brew is not installed")
        print()
        print("Install the brew package manager by following the instructions at https://brew.sh/")
        print("Definitely let us know if you need any help with this!")
        print()
        print("Once brew is installed, run this file again to complete the installation of cmu-graphics")

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print("Hmmm, something unexpected went wrong when checking for brew installation.")
        print("Please come get help on Piazza or in office hours.")
        exit(-1)
    else:

        # Check if pycario and pkg-config are installed
        print("Checking if brew packages cairo and pkg-config are installed...")
        try:
            output = subprocess.check_output(["brew", "list"], text=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
            print("Hmmm, something unexpected went wrong when checking brew packages.")
            print("Please come get help on Piazza or in office hours.")
            exit(-1)

        if "cairo" not in output or "pkg-config" not in output:
            if "cairo" not in output:
                print("brew package cairo is not installed")
            if "pkg-config" not in output:
                print("brew package pkg-config is not installed")

            print("Installing brew packages cairo and pkg-config...")
            try:
                # subprocess.check_call(["brew", "install", "cairo", "pkg-config"])
                subprocess.check_call(["brew", "install", "cairo", "pkg-config"])
            except subprocess.CalledProcessError as e:
                print(f"Command failed with return code {e.returncode}")
                print("Hmmm, something unexpected went wrong when installing brew packages.")
                print("Please come get help on Piazza or in office hours.")
                exit(-1)
            print("Successfully installed brew packages cairo and pkg-config")
        else:
            print("Successfully found brew packages cairo and pkg-config")

        print('Installing cmu-graphics on Mac OSX...')
        install('cmu-graphics')
        print()
        print('DONE')

elif platform.system() == "Windows":
    print('Installing cmu-graphics on Windows...')
    install('cmu-graphics')
    print()
    print('DONE')

else:
    print("It looks like you are likely running Linux and thus are probably good at following instuctions. Make sure to follow the instructions at this link before pip installing cmu-graphics: https://pycairo.readthedocs.io/en/latest/getting_started.html")

    response = input("Have you alread installed Pycairo and want to continue to installin cmu-graphics? (Y/n): ")
    if response in ('y', 'Y', 'yes', 'Yes', 'YES', ''):
        print('Installing cmu-graphics on Linux...')
        install('cmu-graphics')
        print()
        print('DONE')
    else:
        print("Please install Pycairo and then run this file again to install cmu-graphics.")
        print("Pycairo installation instructions can be found at https://pycairo.readthedocs.io/en/latest/getting_started.html")

