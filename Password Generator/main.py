from random import choice
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=~`}{|\:;/?.>,<'
password = ''
print('Password Generator\n==================\n')
num = int(input('Number of Passwords: '))
length = int(input('Password Length: '))
for n in range(num):
    password = ''
    for l in range(length):
        
        #choice randomly chooses a character from a string 
        password += choice(chars)
    print(password)
