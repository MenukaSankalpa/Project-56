# src/main.py
import sys
from account_manager import switch_account
from credential_manager import clear_git_credentials
from github_cli import login_github_cli

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <username> <email>")
        sys.exit(1)

    username = sys.argv[1]
    email = sys.argv[2]

    # Clear previous credentials
    clear_git_credentials()

    # Switch to new GitHub account
    switch_account(username, email)

    # Log in via GitHub CLI (if necessary)
    login_github_cli()

    print("Account switch completed successfully.")

if __name__ == "__main__":
    main()
