# src/config_manager.py
import subprocess

def set_global_git_config(username, email):
    """Set global Git configuration for user name and email."""
    print(f"Setting global Git config for {username} <{email}>...")
    subprocess.run(['git', 'config', '--global', 'user.name', username], check=True)
    subprocess.run(['git', 'config', '--global', 'user.email', email], check=True)
    print(f"Git global configuration updated for: {username}")
