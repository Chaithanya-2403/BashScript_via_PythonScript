import subprocess
import sys

def call_bash_script(args):
    # Call the bash script with the provided arguments
    result = subprocess.run(['./call_dotnet.sh'] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Print the output from the bash script (and .NET app)
    print(result.stdout)

if __name__ == "__main__":
    # Capture command-line arguments passed to the Python script
    # Skip the first argument as it's the Python file itself
    args = sys.argv[1:]

    if not args:
        print("No arguments provided to Python script.")
        sys.exit(1)

    # Call the bash script with the provided args
    call_bash_script(args)

