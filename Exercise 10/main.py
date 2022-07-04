# Main file of the Python program.

#import all exercises from 1-7

#exer1

def make_shirt(size, message):
    print("I'll make a " + size + " t-shirt.")
    print('The message "' + message + '" will be printed on it\n')

try:
    make_shirt('large', 'I want spaghetti!')
    make_shirt(message="Let's eat spaghetti!", size='medium')
except:
    print('Size not found! Error!')


#exer2



def make_shirt(size='large', message='I want Spaghetti!'):
    print("I'll make a " + size + " t-shirt.")
    print('The message "' + message + '" will be printed on it\n')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Spaghetti with Hotdog!')

#exer3

def make_album(artist, title,tracks=[]):
    album_info = {
        'artist': artist.title(),
        'title': title.title(),
        }
    try:
        if tracks:
            album_info['tracks']=tracks
            raise Exception("Sorry no tracks with that name")
        return album_info
    except:
        print("Error!")    

album = make_album('Kendrick', 'DAMN.',tracks = 14)
print(album)

album = make_album('Drake', 'More life',tracks =22)
print(album)

album = make_album('Eminem', 'The Marshall Mathers LP')
print(album)


#exer4

from shutil import ExecError


def make_album(artist, title,tracks=[]):
    album_info = {
        'artist': artist.title(),
        'title': title.title(),
        }
    try:
        if tracks:
            album_info['tracks']=tracks
            raise Exception("No album with that name")
        return album_info
    except:
        print("Something went wrong!")

artists_prompt = "Who are the artists that you think of?"
title_prompt = "What are their albums that you like?"

print("Enter Q if you want to quit")

while True:
    artist = input(artists_prompt)
    if artist == 'q':
        break
    
    title = input(title_prompt)
    if title == 'q':
        break
    
    album = make_album(artist, title)
    print(album)

print("nice album!")


#exer5

def show_magicians(magicians):
    try:
        for magician in magicians:
            print(magician.title())
    except:
        print("Magician not found!")

magicians = ['Harry Potter', 'Lord Voldemort', 'Hermoine']
show_magicians(magicians)


#exer6


def show_magicians(magicians):
    try:
        for magician in magicians:
            print(magician)
    except:
        print("Magician not found!")
        
def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Potter', 'Lord Voldemort', 'Hermoine']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

#exer7

def make_sandwich(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        try:
            print("  ...adding " + item + " to your sandwich.")
        except:
            print("Error!")
        print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')



