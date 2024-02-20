import hashlib
import re
import string
from itertools import permutations


# Simple 256 Hash of Hello World

m = hashlib.sha256()

m.update(b'Hello World')
print('The hex digest SHA256 hash for \"Hello World\" is:\n',m.hexdigest())

# Take input from user and hash it using SHA 256

plaintextInput = input('Enter a phrase you would like to hash using SHA 256:\n')

h = hashlib.sha256()
h.update(plaintextInput.encode())

hashedText = h.hexdigest()

print('The SHA256 hash for your input is:', hashedText)


# Now take a pseudo username and password combo, and hash it using multiple hashing algorithms
# SHA256 isn't the only way to hash, as other hashing algorithms will be implemented this time

myUserName = input('Enter a basic username:\n')
myPassWord = input('Now enter your secretive password:\n')

hash224 = hashlib.sha224()
hash256 = hashlib.sha256()
hash384 = hashlib.sha384()
hashMD5 = hashlib.md5()

hash224.update(myPassWord.encode())
hash256.update(myPassWord.encode())
hash384.update(myPassWord.encode())
hashMD5.update(myPassWord.encode())

print('The SHA224 hash for your input is:', hash224.hexdigest())
print('The SHA256 hash for your input is:', hash256.hexdigest())
print('The SHA384 hash for your input is:', hash384.hexdigest())
print('The MD5 hash for your input is:', hashMD5.hexdigest())



# Hashing algorithms are great, but they are succeptible to an attack called a 
# Dictionary Attack, which attacks the hash by using hashes of well-known plaintext
# passwords. These hashes are stored in tables called Rainbow Tables. An example of
# a dictionary attack will be simulated below

myUserName = input('Enter a basic username:\n')
print('We will still use your username from before.')

myNewPassword = input('Enter a new password. It must be a length of 4 or less, and alphanumeric password.\n')

# Check the password

while(True):
    if len(myNewPassword) > 5 or bool(re.match("^[A-Za-z0-9]*$", myNewPassword))==False:
        myNewPassword = input('Enter a new password AND FOLLOW THE DIRECTIONS!!!\n')
    else:
        break
print('My new password is:', myNewPassword)

# hash the password using the SHA256 hashing algorithm

hash1 = hashlib.sha256()
hash1.update(myNewPassword.encode())
hashedPassword = hash1.hexdigest()


## HERE WE WILL MAKE A LIST OF ALL THE POSSIBLE COMBOS OF ALPHANUMERIC PASSWORDS OF LENGTH 4
listUpperCase = list(string.ascii_uppercase)
listLowerCase = list(string.ascii_lowercase)
listNumbers = list(string.digits)
alphaNumericList = listUpperCase + listLowerCase + listNumbers
# print(len(alphaNumericList))

possiblePasswordList = list(permutations(alphaNumericList,4))
# print(len(possiblePasswordList))
# print(possiblePasswordList[0:10])
for i in range(len(possiblePasswordList)):
    possiblePasswordList[i] = "".join(possiblePasswordList[i])
# print(len(possiblePasswordList))
# print(possiblePasswordList[0:10])



# Now here we run the dictionary attack. Since the password MUST be alphanumeric, and it's
# a relatively short password, a brute force attack with the current system should take a
# short amount of time to guess the password



for currPassword in possiblePasswordList:
    hash2 = hashlib.sha256()
    # First, let's hash the password
    # print('password is:',hashedPassword)
    # print('current password is:', currPassword)
    hash2.update(currPassword.encode())
    hashedCurrPassword = hash2.hexdigest()
    
    if hashedCurrPassword == hashedPassword:
        print('Password has been discovered!')
        print('*********************************************************')
        print('The hash of the original password was:\n', hashedPassword)
        print('*********************************************************')
        print('The hash of the current password is:\n', hashedCurrPassword)
        print('*********************************************************')
        break

print('Program ended')




























