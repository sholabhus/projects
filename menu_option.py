def menu():
    menuOption = int(input("Select an option 1,2 or 3 :"))
    if(menuOption==1):
        print("These are all the running trainers")
    elif(menuOption==2):
        print("These are all the Classics")
    elif(menuOption==3):
        print("These are all the boots and shoes")
    else:
        print("You didn't choose the correct option")


menu()