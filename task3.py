import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(path, indent_level=0):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(Fore.BLUE + '  ' * indent_level + f"[DIR] {entry.name}")
                    print_directory_structure(entry.path, indent_level + 1)
                else:
                    print(Fore.GREEN + '  ' * indent_level + f"[FILE] {entry.name}")
    except PermissionError:
        print(Fore.RED + '  ' * indent_level + "[ACCESS DENIED]")
    except FileNotFoundError:
        print(Fore.RED + '  ' * indent_level + "[NOT FOUND]")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task3.py <path_to_directory>")
    else:
        directory_path = sys.argv[1]
        if os.path.isdir(directory_path):
            print(f"Directory structure for {directory_path}:")
            print_directory_structure(directory_path)
        else:
            print(Fore.RED + "Error: The provided path is not a directory or does not exist.")
