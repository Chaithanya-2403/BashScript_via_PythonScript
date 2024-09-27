#!/bin/bash

# Check if any arguments are passed
if [ $# -eq 0 ]; then
    echo "No arguments provided to bash script."
    exit 1
fi

# Path to your .NET application
dotnet_app_path="/home/chaithanya/Documents/Bash_via_Python/linux-x64/PythonBashScripting.dll"

# Run the .NET application with arguments
dotnet "$dotnet_app_path" "$@"
