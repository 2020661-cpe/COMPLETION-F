#Gamara, Diane E.
#BSCPE
#Pizza Toppings

prompt = "What topping would you like me to put on your pizza?\n"
prompt += "Enter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("I'll add ",topping, "to your pizza.")
    else:
        break

