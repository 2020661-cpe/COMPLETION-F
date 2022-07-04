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

