import secrets
import string


def strong_password(length, number, exclude, include):
    default_list = string.ascii_letters + string.digits + string.punctuation
    
    charset = ''.join([char for char in default_list if char not in exclude])
    charset = charset.strip()
    
    if include != '':   
        include = ''.join(set(include)) # gets rid of duplicate characters
        charset = include   
    elif exclude != '':
        charset = charset.strip(exclude)
    
    # print(f"this is exclude:  {exclude}")
    # print(f"this is include:  {include}")
    # print(f"this is charset:  {charset}")


    passwords = []
    for k in range(number):
        password = ''
        for _ in range(length):
            password += secrets.choice(charset)
        passwords.append(password)

    return passwords
