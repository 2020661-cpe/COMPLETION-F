
try:
    
    person = {
        'first_name': 'Diane',
        'last_name': 'Endaya',
        'age': 19,
        'city': 'Lipa',
        }

    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])

except:
     
    print('Error! Person not found')
    
    
    
try:
    fav_numbers = {}
    'Dan': 44
    'Dam': 22
    'Dyn': 24
    'Dhine': 50
    'Dani': 11


    num = fav_numbers['Dan']
    print("Dan's favorite number is " + str(num))

    num = fav_numbers['Dam']
    print("Dam's favorite number is " + str(num))

    num = fav_numbers['Dyn']
    print("Dyn's favorite number is " + str(num))

    num = fav_numbers['Dhine']
    print("Dhine's favorite number is " + str(num))

    num = fav_numbers['Dani']
    print("Dani's favorite number is " + str(num))
except:
    print("Error! Person's age not found")






try:
    rivers = {
    'Nile': 'Egypt',
    'Amazon': 'South America',
    'Congo': 'Africa',
    'Amur': 'Bangladesh',
    'Yangtze': 'China',
    }

    for river, country in rivers.items():
        print("The " + river.title() + " flows through " + country.title() + ".")

    print("\nThe following rivers are included in this data set:")
    for river in rivers.keys():
        print("- " + river.title())

    print("\nThe following countries are included in this data set:")
    for country in rivers.values():
        print("- " + country.title())

except:
    print("Error! No river found!")

