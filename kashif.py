from random import *

guess=""

password=input("password")

letters =["a","b","c","d","f","e"]

while(guess != password):
    Guess=""
    for letter in password:
        guessletter=letters[randint(0,25)]
        guess=str(guessletter) + str(guess)
print("password is successfully cracked !")
input("")
