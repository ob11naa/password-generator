#password generator

import random 
print('INPUT PASSWORD')

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()?ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password = ''

for x in range(16):
    password += random.choice(chars)
    
print(password)