import re
test_pass = ['dh82DSFDA', "StrongP@ssw0rd", "Secur3P@ss", "P@ssw0rd123", "L0ngAnd$ecure", "*SuperStr0ng*", 
             "Pa$$w0rd!123", "1234ABCDEfgh", "SecurePa$$", "password", "123456", "qwerty", "letmein", 
             "admin", "abc123", "iloveyou", "password123"]

for i in test_pass:
    if not re.search(r'[A-Z]', i) or not re.search(r'[a-z]', i) or not re.search(r'[0-9]', i) or len(i)<8:
        print(i, 'is invalid')
    else:
        print(i, 'is valid')