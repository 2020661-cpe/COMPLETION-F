try:
    car = input ("What kind of rental car do you prefer?")
    print ('Let me see if I can find you a', car)

except Exception as error:
    print(error)