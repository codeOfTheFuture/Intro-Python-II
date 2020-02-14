from room import Room
from player import Player
from item import Item

# Declare all the items
item = {
    'health':    Item('Health', 
                      'Increases your health'),
    'sword':     Item('Sword', 
                      'Sword will slay an enemy'),
    'slingshot': Item('Slingshot', 
                      'Slingshot will reduces enemy\'s health'),
    'blaster':   Item('Blaster', 
                      'Blaster will kill an enemy'),
    'shield':    Item('Shield', 
                      'Shield will protect you from enemy fire'),
    'armour':    Item('Armour', 
                      'Armour will protect you from enemy fire'),
    'key':       Item('Key',
                      'Key will unlock a chest'),
    'treasure':  Item('Treasure',
                      'Treasure will add to your $$')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['health'], item['shield']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['sword'], item['slingshot']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['blaster'], item['shield']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['key'], item['armour']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['treasure'], item['armour']])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


current_player = Player(input('What is your name? '), room['outside'])

print(f'\nYou are playing as {current_player.name}.\n')
print('\n--------------------------------------------\n')
print(current_player.current_room, '\n\n')
print(current_player.current_room.show_items())
print('\n--------------------------------------------\n')

while True:
    print(current_player.name)
    print('Your Items: ')

    if len(current_player.items) < 1:
        print('    You have no items')
    else:
        for item in current_player.items:
            print(f'    {item.name}\n    {item.description}\n')

    print('\nWhat would you like to do next?')

    cmd = input('-> ').lower().split(' ')

    if len(cmd) == 2:
        action = cmd[0]
        item = cmd[1]

        if action == 'take':
            current_player.add(item)

        elif action == 'drop':
            current_player.drop(item)

    elif len(cmd) == 1:
        cmd = cmd[0]
        if cmd in ['n', 's', 'e', 'w']:
            print('\n--------------------------------------------\n')
            current_player.change_room(cmd)
            current_player.current_room.show_items()
            print('\n--------------------------------------------\n')
        elif cmd == 'q':
            print('Goodbye!')
            break
    else:
        print('I did not understand your command!')

    # while True:
    # print(current_player.name)
    # print(current_player.current_room.name)
    # print(current_player.current_room.description)

    # direction = input('Choose Direction: ')

    # if direction == 'n':
    #     if current_player.current_room.name == 'Outside Cave Entrance':
    #         current_player.change_room(room['outside'].n_to)
    #     elif current_player.current_room.name == 'Foyer':
    #         current_player.change_room(room['foyer'].n_to)
    #     elif current_player.current_room == 'Narrow Passage':
    #         current_player.change_room(room['narrow'].n_to)
    #     else:
    #         print('Please choose a different direction')
    # elif direction == 's':
    #     if current_player.current_room.name == 'Foyer':
    #         current_player.change_room(room['foyer'].s_to)
    #     elif current_player.current_room.name == 'Grand Overlook':
    #         current_player.change_room(room['overlook'].s_to)
    #     elif current_player.current_room.name == 'Treasure Chamber':
    #         current_player.change_room(room['treasure'].s_to)
    #     else:
    #         print('please choose a different direction')
    # elif direction == 'e':
    #     if current_player.current_room.name == 'Foyer':
    #         current_player.change_room(room['foyer'].e_to)
    #     else:
    #         print('please choose a different direction')
    # elif direction == 'w':
    #     if current_player.current_room.name == 'Narrow Passage':
    #         current_player.change_room(room['narrow'].w_to)
    # elif direction == 'q':
    #     break
    # else:
    #     print('Please choose n for North, s for South, e for East, w for West, or q to quit')

    # if player_choice == 'm':
    #     cmd = input('Choose a direction: ').lower()
    #     if cmd in ['n', 's', 'e', 'w']:
    #         print('\n--------------------------------------------\n')
    #         current_player.change_room(cmd)
    #         current_player.current_room.show_items()
    #         print('\n--------------------------------------------\n')
    #     elif cmd == 'q':
    #         print('Goodbye!')
    #         break
    # elif player_choice == 'p':
    #     print('Which Item would you like to pick up?: ')
    #     for item in current_player.current_room.room_items:
    #         print(f'{item}\n')
    #     selected_item = input('->')
    #     current_player.add(selected_item)
    # elif player_choice == 'd':
    #     print('Which of your items would you like to drop?: ')
    #     for item in current_player.items:
    #         print(f'{item}\n')
    #     selected_item = input('->')
    #     current_player.drop(selected_item)
    # else:
    #     print('Please choose n for north, s for south, e for east, w for west, or q to quit')