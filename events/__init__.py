import os
import importlib

# Get the directory of the current file
package_dir = os.path.dirname(__file__)

# Loop through all files in the package directory
for module_name in os.listdir(package_dir):
    # Check if the file is a Python file but not __init__.py
    if module_name.endswith('.py') and module_name != '__init__.py':
        # Remove the .py extension to get the module name
        module = module_name[:-3]
        # Import the module
        importlib.import_module(f".{module}", package=__name__)