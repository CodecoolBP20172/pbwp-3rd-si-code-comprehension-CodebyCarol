'''This game is a "find out what number I am thinking about" game,
with 6 possible guess'''

import random #imports the random module from python

guessesTaken = 0 #introduce a variable, which is a number, for the start, zero.

print('Hello! What is your name?')#prints a string, asking the user name
myName = input() #introduce a variable, which is a user imput, the user's name.

number = random.randint(1, 20) #our new variable is a random integer between 1-20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
#prints the conundrum, with the user's name
while guessesTaken < 6: #until the number of guesses is lower than 6
    print('Take a guess.') #prints out this string
    guess = input()#getting a user imput (a guess)
    guess = int(guess)#transform the user imput to integer

    guessesTaken += 1 #the variable increased by one

    if guess < number: #if the user's guess is lower than the random generated number
        print('Your guess is too low.') #prints this reply

    if guess > number: #if the user's guess(imput) is bigger than the random
                       #generated number
        print('Your guess is too high.')#prints this reply

    if guess == number: #this boolean inspects if user imput equals to the
                        #random generated number
        break #breaks the while loop

if guess == number: #after while loop ended, inspects if user input equals to
                    #the random generated number
    guessesTaken = str(guessesTaken) #transform the guessesTaken variable from
                                     #number to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
#prints out a reply, containing the user's name and the guessesTaken variables
if guess != number: #after the while loop ended, and the user input not equals
                    #to the random generated number
    number = str(number) #transforms the random generated number to string
    print('Nope. The number I was thinking of was ' + number)
#prints out the solution
