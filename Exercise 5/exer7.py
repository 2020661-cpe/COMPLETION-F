#Gamara, Diane E.
#BSCPE
#Movie Tickets

prompt = 'The prices ranges based on how old you are, so you might wanna give me your ages.\n'
prompt += 'Enter "quit" when you are finished :'

active = True

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print ("You have a free ticket!")
    elif age ==3 and age < 13:
        print ("Your ticket cost 10 pesos!")
    else :
        print ("Your ticket cost 15 pesos!")