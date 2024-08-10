from getpass import getpass


def get_credential(prompt=''):
    password = None
    while not password:
        password = getpass(prompt)
        password_verify = getpass("Retype your password: ")
        if password_verify != password:
            print("Password not match")
            password = None
    return password
