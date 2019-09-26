
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.

def display_inventory(inventory):
        for i, s in inventory.items():
            print(i + ": " + str(s))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1


def print_table(inventory, order=None):

    if order == None:
        tmp = list(inventory.items())
        Lenght = [len(i) for i in inventory] 
        x = max(Lenght)
        if x < 9:
            x = 9
        print("-" * (x + 8))
        print("item name".rjust(x), "|", "count".rjust(5))
        print("-" * (x + 8))
        for i in range(len(tmp)):
            print((tmp[i][0]).rjust(x), "|", (str(tmp[i][1])).rjust(5) )
        print("-" * (x + 8))
    elif order == "count,desc":
        tmp = list(inventory.items())
        inv_tmp = sorted(tmp, key=lambda thing: thing[1], reverse = True)
        Lenght = [len(i) for i in inventory] 
        x = max(Lenght)
        if x < 9:
            x = 9
        print("-" * (x + 8))
        print("item name".rjust(x), "|", "count".rjust(5))
        print("-" * (x + 8))
        for i in range(len(inv_tmp)):
            print((inv_tmp[i][0]).rjust(x), "|", (str(inv_tmp[i][1])).rjust(5))
        print("-" * (x + 8))
    elif order == "count,asc":
        tmp = list(inventory.items())
        inv_tmp = sorted(tmp, key=lambda thing: thing[1])
        Lenght = [len(i) for i in inventory]  ##   Itt tartok 
        x = max(Lenght)
        if x < 9:
            x = 9       
        print("-" * (x + 8))
        print("item name".rjust(x), "|", "count".rjust(5))
        print("-" * (x + 8))
        for i in range(len(inv_tmp)):
            print((inv_tmp[i][0]).rjust(x), "|", (str(inv_tmp[i][1])).rjust(5))
        print("-" * (x + 8))


def import_inventory(inventory, filename="import_inventory.csv"):
    inv_temp = []
    tmp = []
    with open (filename, "r") as f:
        inv_temp.append(f.readline())

    for i in inv_temp:
        tmp.append(i.split(",",-1))

    for i in tmp[0]:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    tmp = []
    for key, value in inventory.items():
        for x in range(value):
            tmp.append(key)

    with open(filename, "w") as f:
        for item in tmp:
            if x != len(tmp)-1:
                f.write("%s," % item)
                x+=1
            else:
                f.write(item)
        

#inv = {'rope': 1, 'gold coin': 2, 'dagger': 1, 'arrow': 1}
#dragon_loot = ['alma','gold coin', 'dagger', 'gold coin', "orban balkeze", 'gold coin', 'ruby', 'alma']
#export_inventory(inv)
#print_table(inv)
#print_table(inv, "count,desc")
#print_table(inv, "count,asc")
#import_inventory(inv, "test_inventory.csv")
#print_table(inv, "count,asc")