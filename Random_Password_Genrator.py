import secrets
import string
passwd = ''
letter = string.ascii_letters
number = string.digits
symbl = string.punctuation
alphabet = letter+number+symbl
passwd_len = int(input("Enter the Length of password:"))
for i in range(passwd_len):
    passwd=passwd+''.join(secrets.choice(alphabet))
print(f'PASSWORD:- {passwd}')
