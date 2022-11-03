#! python3

### A Fantasy Game Inventory program ###

inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

dragon_loot = [
    'gold coin',
    'dagger',
    'ruby',
    'gold coin',
    'gold coin',
    'dragon\'s tooth'
]


def display_inventory(inventory):
    """ Displays the player ionventory with ammount item.

    Args:
        inventory (Dictionary): A dictionary over items and the ammount of the items.
    """

    print('Inventory:')
    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v

    print('Total number of items: ' + str(item_total))


def add_to_inventory(inventory, added_items):
    """ Adds items to the inventory

    Args:
        inventory (Dictionary): A dictionary over items and the ammount of the items.
        added_items (List): A list over items to add to the inventory.
    """

    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    print('Items added to your inventory.')


display_inventory(inventory)
add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
