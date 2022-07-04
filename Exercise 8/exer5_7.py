try:
    message = "\nHow old are you?"
    message += "\nEnter 'quit' when you are finished.\n"

    while True:
        age = input(message)
        if age == 'quit':
            break

        age = int(age)
        if age < 3:
            print("You are free!")
        elif age >3 and age < 13:
            print("Your ticket is 10 pesos!")
        else:
            print("Your ticket is 15 pesos!")

except Exception as error:
    print(error)