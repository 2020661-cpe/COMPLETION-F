
items = ('Prawn Curry', 'Glazed Ham', 'Pork Loin', 'Decadent Veal', 'Coleslaw',)

print("You can choose from the following menu items:")
for item in items:   
    print("- " + item)

items = ('Prawn Curry', 'Glazed Ham', 'Pork Loin', 'Decadent Veal', 'Coleslaw',)

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in items:
    print("- " + item)


movie = 'Green Miles'
genre = ['fantasy', 'drama',]
anime = ['One Piece', 'Tokyo Ghoul',]

print("I would like to watch an", genre,"anime like ",anime) 
 


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



cities = ["Korea", "Spain", "Japan", "Australia", "Maldives"]
print(cities)
print(sorted(cities))
print(cities)
print(sorted(cities, reverse=True))
print(cities)
cities.reverse()
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse = True)
print(cities)



flavors = ['Pork Lomi','Pancit Lomi', 'Chicken Lomi']

for item in flavors:
    print("I want to eat " + item)
    
print('When the weather is cold, I love eating lomi')




cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


