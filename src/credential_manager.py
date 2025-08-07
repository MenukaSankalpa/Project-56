# src/credential_manager.py
import subprocess
import os

def clear_git_credentials():
    """Clear any saved Git credentials from the credential manager."""
    print("Clearing stored Git credentials...")

    # clear credential cache code
    subprocess.run(['git', 'credential-cache', 'exit'], check=True)

    if os.name == 'nt':  # fro windows
        subprocess.run(['git', 'credential-manager', 'erase'], check=True)
    elif os.name == 'posix':  # for macOS/Linux
        subprocess.run(['git', 'credential-osxkeychain', 'erase'], check=True)
    
    print("Git credentials cleared !")
