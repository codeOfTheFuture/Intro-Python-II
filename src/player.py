# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []

  def change_room(self, direction):
    new_room = getattr(self.current_room, f'{direction}_to')

    if new_room != None:
      self.current_room = new_room
      print(f'{self.current_room}\n')
    else:
      print('You cannot move in that direction')

  def add(self, selected_item):
    if len(self.current_room.room_items) == 0:
      print('This room does not have any items!')
    else:
      for item in self.current_room.room_items:
        if item == selected_item:
          self.current_room.room_items.remove(item)
          self.items.append(item)
          print(f'You are now carrying: {item}\n')

  def drop(self, selected_item):
    if len(self.items) == 0:
      print('You do not have any items')
    else:
      for item in self.items:
        if item == selected_item:
          self.items.remove(item)
          self.current_room.room_items.append(item)
          print(f'You are no longer carrying {item}\n')