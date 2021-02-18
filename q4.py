print("########################################")
print("MYPY PHONE BOOK")
print("########################################")

#Prompt the user to choose an option
def print_menu():
    print('1 : Add New Entry')
    print('2 : Delete Entry')
    print('3 : Update Entry')
    print('4 : Lookup Number')
    print('5 : QUIT')

numbers = {}
choice = 0
print_menu()
while choice != 5:
    choice = int(input("Choose any number between 1 and 5: "))

    #Updating an entry
    if choice == 3:
        y=input("Enter name whose number needs update:")
        for x in numbers.keys():
            if x==y:
                numbers[x]= int(input("Enter new number:"))
                print("Name: ", x, "\tNumber:", numbers[x])
                print()

    #Adding new entry
    elif choice == 1:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        if phone in numbers.values():
            #if the user enters the same number
            print("Phone number already exists")
        else:
            numbers[name] = phone

    #Deleting an entry
    elif choice == 2:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")

    #Looking up any entry
    elif choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")

    #Quitting if the user decides to quit
    elif choice != 5:
        print_menu()
