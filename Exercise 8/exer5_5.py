try:
    message = "What topping would you like on your pizza?\n"
    message += "Enter 'quit' when you are finished: "
    prompt = "a hundred bucks"
    while True:
        topping = input(prompt)
        if topping != 'quit':
            print("I'll add", topping,"to your pizza.")
        else:   
            break

except Exception as error:
                        print(error)