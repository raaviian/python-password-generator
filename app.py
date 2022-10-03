import secrets
from sre_parse import SPECIAL_CHARS
import string
from unicodedata import digit

#delare what we need
letters = string.ascii_letters
digits = '0123456789'
special_chars = string.punctuation

#password combination
alphabet = letters + digits + special_chars

#password length
pwd_length = 8

#looping for randomize the password
pwd = ''
for i in range (pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

#password output result
print('Result:')
print(pwd)
print('Is strong recommended password')

#while True:
    #pwd = ''
    #for i in range(pwd_length):
        #pwd += ''.join(secrets.choice(alphabet))

      #sum(char in digits for char in pwd)>=2):
          #break
#print(pwd)

#Raaviian
#UTHM