account-switcher-python/
│
├── assets/                     # (Optional) Store assets like images, icons, etc.
│
├── config/                     # Store configuration files (e.g., Git configuration, tokens)
│   └── .gitconfig              # Global Git configuration if needed
│
├── src/                        # Source code for the program
│   ├── __init__.py             # Marks this folder as a package
│   ├── account_manager.py      # Handles account-related tasks (add, remove, switch)
│   ├── credential_manager.py   # Handles Git credentials management
│   ├── github_cli.py           # Handles GitHub CLI authentication
│   ├── config_manager.py       # Configures global settings for Git (user name, email)
│   ├── main.py                 # Main entry point to run the program
│
├── tests/                      # Unit tests and integration tests
│   ├── __init__.py
│   ├── test_account_manager.py
│   ├── test_credential_manager.py
│   └── test_github_cli.py
│
├── requirements.txt            # List of dependencies for Python project
├── README.md                   # Project documentation
└── LICENSE                     # License information (MIT, GPL, etc.)
