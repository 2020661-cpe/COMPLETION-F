
def show_magicians(magicians):
    try:
        for magician in magicians:
            print(magician.title())
    except:
        print("Magician not found!")

magicians = ['Harry Potter', 'Lord Voldemort', 'Hermoine']
show_magicians(magicians)

