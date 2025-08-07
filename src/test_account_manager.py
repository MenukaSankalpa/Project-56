# tests/test_account_manager.py
import subprocess
from src.account_manager import remove_existing_github_account, add_new_github_account

def test_remove_existing_github_account():
    """Test removing existing GitHub credentials."""
    subprocess.run = lambda *args, **kwargs: None  # mocking subprocess call
    remove_existing_github_account()
    assert True  # if no exceptions, the test passes

def test_add_new_github_account():
    """Test adding a new GitHub account."""
    subprocess.run = lambda *args, **kwargs: None  # mocking subprocess call
    add_new_github_account('test_user', 'test_user@example.com')
    assert True  # if no exceptions, the test passes
