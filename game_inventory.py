
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.

def display_inventory(inventory):
        for i, s in inventory.items():
            print(i, ":", s)

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] = inventory[i] +1
        else:
            inventory[i] = 1

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inv_2 = list(inv.items())
inv_3 = sorted(inv_2, key=lambda thing: thing[1], reverse = True)


 


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''

    if order == None:
        for i, s in inventory.items():
            print(i, ":", s)  
    elif order == "count,desc":
        tmp = list(inventory.items())
        inv_tmp = sorted(tmp, key=lambda thing: thing[1])
        Lenght = [len(i) for i in inventory]  ##   Itt tartok 
        print(Lenght)
        for i in inv_tmp:
            print(i)
    elif order == "count,asc":
        tmp = list(inventory.items())
        inv_tmp = sorted(tmp, key=lambda thing: thing[1], reverse = True ) 
        for i in inv_tmp:
            print(i)        
    pass


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''

    pass


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    pass



#print_table(inv)
print_table(inv, "count,desc")
#print_table(inv, "count,asc")