
my_string = input("Enter a text: ")  # enter a string
my_string = my_string.casefold()  # changes the string to one case to ensure the cases of the word do not interfere
rev_string = reversed(my_string)  # reverse string

if list(my_string) == list(rev_string):  # check if string input is equal to its reverse
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")





