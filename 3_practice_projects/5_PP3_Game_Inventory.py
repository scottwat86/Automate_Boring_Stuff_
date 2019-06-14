#               Automate the Boring Stuff with Python 3
#               Ch 5 -  Practice Project - Fantasy Game Inventory
#               By Scott Watson

# PART 1
def displayInventory(backpack):
    print('Inventory:')

    total = 0
    for k, v in backpack.items():
        print(str(v) + ' ' + k)
        total += v
    print('\nTotal number of items:  ' + str(total))

# PART 2
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) # Ensures the item key is in the dict
        inventory[item] +=1


# backpack = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
# displayInventory(backpack)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inv)
print('BASH! You killed the dragon!\n')
_ = input('Press any key to loot.\n')
addToInventory(inv, dragonLoot)
displayInventory(inv)
