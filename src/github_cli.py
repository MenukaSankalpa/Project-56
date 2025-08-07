# src/github_cli.py
import subprocess

def login_github_cli():
    """Authenticate using GitHub CLI."""
    print("Logging into GitHub via GitHub CLI...")
    subprocess.run(['gh', 'auth', 'login'], check=True)
    print("Logged in to GitHub CLI !")

