
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

