# password generator


import string #we imported the string
from random import* #imported the random module

lower="abcdefghijklmnopqrstuvwxyz" # its data from which the password will generated
upper_1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"# its data from which the password will generated
num=1234567890# its data from which the password will generated
spcial="!@#$*?"# its data from which the password will generated
a= str(lower)+str(upper_1)+str(num)+str(spcial) # we uses string to add the whole password data  together
b="".join(choice(a) for i in range (randint(8,16))) # here we uses the .join( )method to join the whole data
#data together and in join we passed the choice method which will randomly choice the password and it will be in the
#range of 8 to 16

print(b) #finally printed the password