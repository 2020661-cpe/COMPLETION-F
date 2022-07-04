


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

