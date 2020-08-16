import random as rd
'''importing a random library as rd'''

Generate = rd.randint(0,20)
Guess = int(input('The number is',  ))
if  Guess ==  Generate :
    print("your guess is absolutely correct")
if Guess > Generate :
    print("your guess is too high try again")
elif Guess < Generate :
    print("your guess is too low try again")




