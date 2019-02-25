#Kyung Min Yeo
#CSC4980 HW2
import hashlib
from urllib2 import urlopen #needed for handling the url
import time

url = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").read()
passlist = str(url).split("\n")

inputHash = raw_input("Enter a SHA-1 hash value for the program to attempt to break. \n")

count = 0
startTime = time.time()

for password in passlist:
    count+=1
    print '\nAttempt', count, ':', password
    if inputHash == 'ece4bb07f2580ed8b39aa52b7f7f918e43033ea1':
        password += 'f0744d60dd500c92c0d37c16174cc58d3c4bdd8e'  #add the salt value if part c)
    sha = hashlib.sha1(password)
    print 'hexdigest:', sha.hexdigest()
    if hashlib.sha1(password).hexdigest() == inputHash:  #if the hexadecimal representation of the digest matches the user input
        print "\nBrute force successful. The original string is: ", password
        print "Program execution time: ", time.time() - startTime , ' seconds, after ',count, ' attempts'
        exit()
print "Unable to brute force the SHA-1 hash value." #This point should not be reached  