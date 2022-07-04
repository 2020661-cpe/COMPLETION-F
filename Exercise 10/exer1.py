
def make_shirt(size, message):
    print("I'll make a " + size + " t-shirt.")
    print('The message "' + message + '" will be printed on it\n')

try:
    make_shirt('large', 'I want spaghetti!')
    make_shirt(message="Let's eat spaghetti!", size='medium')
except:
    print('Size not found! Error!')

