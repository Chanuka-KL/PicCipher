import os
import subprocess
import sys

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages and their versions
required_packages = [
    "Pillow==9.3.0",
    "colorama==0.4.6"
]

def main():
    print("Installing required packages...")

    for package in required_packages:
        try:
            print(f"Installing {package}...")
            install(package)
            print(f"{package} installed successfully.")
        except Exception as e:
            print(f"Failed to install {package}. Error: {e}")
    
    print("All packages installed successfully!")

if __name__ == "__main__":
    main()