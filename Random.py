import random

random_int = random.randint(1, 100)
guess =0  # set the counter to 0
print("")
name = input("What is your name? ")  # ask user's name
print("Hello, {} I am thinking of a number between 1 and 100".format(name)) #print output

while guess < 6:
    guess = guess + 1   # increament
    guess_num = int(input("Guess the number :" ))  # ask user for guess and convert to integer
    guess_left =str(6 -guess)   # info user guess remainder
   # print("Computer's Number is: {}".format(random_int))

    if guess_num < random_int:
        print("Incorrect, Your number is too low. Please Try again") # print
        print("")
        print("You have {} guesses left".format(guess_left)) #print no of guess left
        print("")

    elif guess_num > random_int:
        print("Incorrect, Your number is  too high.Please Try again") #print
        print("")
        print("You have {} guesses left".format(guess_left)) #print no of guess left
        print("")

    else:
        print("Congratulations {} you've won".format(name)) #print
        break
