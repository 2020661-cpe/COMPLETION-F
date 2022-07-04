
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



