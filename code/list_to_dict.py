def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total+=v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item]= inventory.get(item, 0)+1
    return inventory

inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)