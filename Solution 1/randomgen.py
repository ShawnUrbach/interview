import random
import string
from random import choice
from string import ascii_uppercase

text_file = open("Random.txt", "w")
for i in range (1,10000):
    string=str(random.randint(1,999))
    for x in range(1):
        string = string + (''.join(choice(ascii_uppercase) for i in range(random.randint(1,1000))))+'\n'
        text_file.writelines(string)
    print (string)
text_file.close()
