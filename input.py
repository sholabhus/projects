
def get_user_input_boolean():  # function to get a boolean value from the user and return the value as boolean
    user_input = "zzz"  # set the initial value of user_input so the loop runs at least once

    while user_input != "True" and user_input != "False":  # check if user has entered one of the required strings
        user_input = input("Enter true or false")
        if user_input == "True":
            user_input_boolean = True
        else:
            user_input_boolean = False

        return user_input_boolean

#start the main program
a = get_user_input_boolean()
b = get_user_input_boolean()

#print the result
print(str(a) + "AND " + str(b) + "is....")
print(a and b)