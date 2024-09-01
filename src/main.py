import argparse
from random_gen import strong_password
import pyperclip
# import xclip

parser = argparse.ArgumentParser(
                    prog='Strong password generator',
                    description='Generates a strong password. Defaults to 3 passwords, of 16 characters (with replacement), and shows the password, unless otherwise specified.',
                    usage='PROG [options]')

parser.add_argument('-l', '--length',type=int, default=16, help='The length of the password')     

# group_show = parser.add_mutually_exclusive_group()
parser.add_argument('-n', '--number', type=int, default=3, help='How many passwords to generate')
parser.add_argument('-c', '--copy', help='To hide the password generated, and copy one password to clipboard instead. Default is false', action='store_true', default=False)  # on/off flag

group_charset = parser.add_mutually_exclusive_group()
group_charset.add_argument('-e', '--exclude', type=str, default='', help='Characters to exclude from charset, due to password filters. Use excape characters.')
group_charset.add_argument('-i', '--include', type=str, default='', help='Use a custom charset, due to password filters. Use escape characters.')

args = parser.parse_args()

passwords = strong_password(length = args.length, 
                            number = args.number, 
                            exclude=args.exclude, 
                            include = args.include)


if args.copy == True:
    pyperclip.copy(passwords[0])
    pyperclip.paste()
    print(f"Password copied to clipboard.")

else:
    for i in range(len(passwords)):
        pass_fmt = f"Password {i+1}: {passwords[i]}"
        print(pass_fmt)
