try:
    sn = "Diane"
    add = "Muntingpulo, Lipa City"
    prog = "BSCPE"

    print (sn)
    print (add)
    print (prog)
    
except:
    print('Name not found')    
    
try:
    name = 'D,'
    message = '\nBe patient. Always.'

    print (name + message)

except:
    print('Name not found')
    
try:
    name = 'Aven'
    m = name.upper()
    n = name.lower()
    o = name.title()

    print (m)
    print (n)
    print (o)

except:
    print('Name not found')
    
try:
    r = '\tBenjamin Franklin once said, "Well done is \n\t\tbetter than well said.'
    print (r)
    
except:
    print("Sentence can't be found")   
    
try:
    famous_person = 'Benjamin Franklin'
    quote  = ' "Well done is better than well said."'

    print (famous_person + ' once said,'+ quote)
    
except:
    print("Famous person can't be found")
    
try:
    p = 4 + 4
    q = 2 * 2 * 2
    r = 10 - 2
    s = 16 / 2
    print (p)
    print (q)
    print (r)
    print (s)
    
except:
    print("Error")

try:
    t = str (20)
    u = '\nWhat do you get when you take ten and divide it by half?\n'
    print ( 'Riddle Time!' + u + t + '!' )
    
except:
    print("Error")
    
try:
    ball_color = 'green'

    if ball_color == 'green':
        print ('Congratulations you just earned 5 points!')
        
except:
    print('Error! Enter a real color')
    
try:
    ball_color = 'green'
    if ball_color == 'green':
        print ('Congratulations you just earned 5 points!')
    else:
        print ('Congratulations you just earned 10 points!')
        
except:
    print("Error! Enter a valid color")

try:
    ball_color = 'yellow'
    if ball_color == 'green':
        print ('Congratulations you just earned 5 points!')
    elif ball_color == 'yellow':
        print ('Congratulations you just earned 10 points!')
    elif ball_color == 'red':
        print ('Congratulations you just earned 15 points!')
    
except:
    print("Error! Enter a valid color")
        
try:
    car = input ("What kind of rental car do you prefer?")
    print ('Let me see if I can find you a', car)

except Exception as error:
    print(error)
    
try:
    group = input ('How many people are in your group?')
    group = int(group)

    if group > 10:
        print ("I'm afraid your table is not available right now. We're very sorry for the inconvinience but you're going to have to wait a little while.")
    else :
        print ("We're happy to say that your table is now available.")
        
except Exception as error:
    print(error)
    
try:
    num = input ("What's your favorite number?")
    num = int(num)

    if num % 10 == 0:
         print ('Your favorite number is a multiple of 10')
    else :
        print ("Your favorite number isn't a multiple of 10")

except Exception as error:
    print(error)
    
try:
    group = input ('How many people are in your group?')
    group = int(group)

    if group > 10:
        print ("I'm afraid your table is not available right now. We're very sorry for the inconvinience but you're going to have to wait a little while.")
    else :
        print ("We're happy to say that your table is now available.")
        
except Exception as error:
    print(error)

try:
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
    

except Exception as error:
        print(error)
        
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
    
try:
    num = 2

    while num < 5:
        print (num)
        
except Exception as error:
    print(error)

try:
    friends = ['Diane', 'Lala', 'Sab']

    print(friends[0])
    print(friends)


    print(friends[1])
    print(friends)


    print(friends[-1])
    print(friends)
    
except Exception as error:
	print(error)
	
try:
    friends = ['Diane', 'Lala', 'Sab']
    print(friends[0])
    print('I hope to see you as soon as I get home.')

    print(friends[1])
    print('Do your homework as soon as you get home.')

    print(friends[-1])
    print('Just stay wherever you are and I will get you in a second.')
    

except Exception as error:
	print(error)

try:
    action = ['One Piece', 'Black Clover', 'HunterxHunter']
    romance = ['Your Name', 'wethering With You', 'Silent Voice']
    thriller = ['Death Note', 'Tokyo Goal', 'Psycho Pass']

    print(action)
    print(action[0])
    print('I will probably watch this first, since it was my first choice among all the other choices.')

    print(thriller)
    print(thriller[1])
    print("I'm actually torn because I heard this is a good watch too.")
    
except Exception as error:
	print(error)

try:
   items = ('Prawn Curry', 'Glazed Ham', 'Pork Loin', 'Decadent Veal', 'Coleslaw',)
    
   print("You can choose from the following menu items:")
   for items in(items):
    print(" " + items)

   items = ('Prawn Curry', 'Glazed Ham', 'Pork Loin', 'Decadent Veal', 'Coleslaw',)

   print("\nOur menu has been updated.")
   print("You can now choose from the following items:")
   for items in(items):
    print(" " + items)

except Exception as error:
                         print(error)


	
try:
    movie = 'Green Miles'
    genre = ['fantasy', 'drama',]
    anime = ['One Piece', 'Tokyo Ghoul',]

    print("I would like to watch an", genre,"anime like ",anime) 
 


except Exception as error:
    print(error)

try:
   locations = ['New York', 'California', 'Seoul', 'Tokyo', 'Bali']

   print("Original order:")
   print(locations)

   print("\nAlphabetical:")
   print(sorted(locations))

   print("\nOriginal order:")
   print(locations)

   print("\nReverse alphabetical:")
   print(sorted(locations, reverse=True))

   print("\nOriginal order:")
   print(locations)

   print("\nReversed:")
   locations.reverse()
   print(locations)

   print("\nOriginal order:")
   locations.reverse()
   print(locations)

   print("\nAlphabetical")
   locations.sort()
   print(locations)

   print("\nReverse alphabetical")
   locations.sort(reverse=True)
   print(locations)

except Exception as error:
     		         print(error)


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    