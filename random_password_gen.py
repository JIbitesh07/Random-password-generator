#using import random as the user needs a random password
import random
import random
#taking random input for the length
from random import randint
length=randint(6,15)

#following are the elements of the password
digits='1','2','3','4','5','6','7','8','9'
uppercase='A','B','C','D','E','F','G','H','I','k','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
lowercase='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
special_characters='!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','{','}','[',']' 
res1=digits+lowercase+uppercase+special_characters
#making sure that the password contains at least 1 uppercase letters,1 lowercase letters,1 special_characters and 1 digit
d2=random.choice(digits)
u2=random.choice(uppercase)
l2=random.choice(lowercase)
s2=random.choice(special_characters)
res2=l2+u2+s2+d2
#taking input from the user to print the number of password he wants
number=int(input("enter the number of passwords you wnat"))
#using a "for loop" to generate the password according to its random length and number of passwords  
for i in range(number):
    password="" 
    for j in range(length):
        password=password+random.choice(res1)
#printing the password
    semi_final=list(res2+password)
    random.shuffle(semi_final)
    Final_result="".join(semi_final)
    print("The password is ",Final_result)

