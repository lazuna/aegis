import subprocess

def list_user_accounts():
    result = subprocess.run(['getent', 'passwd'], capture_output=True, text=True)
    user_accounts = result.stdout.splitlines()
    for account in user_accounts:
        username = account.split(':')[0]
        print(f"User: {username}")

list_user_accounts()
