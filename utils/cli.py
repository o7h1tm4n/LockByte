import getpass

def get_password(prompt: str = "Enter password: ") -> str:
    password = getpass.getpass(prompt)
    return password