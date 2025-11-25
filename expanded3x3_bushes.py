def harvest():
    print('harvest')

def do_a_flip():
    do_a_flip = 'flip'

def get_world_size():
    get_world_size = 'size'

def plant():
    plant = 'size'

def can_harvest():
    can_harvest = 'plant -> harvest'

def move():
    move = 'North, South, East, West'

def till():
    till = 'till'
class Entities():
    Grass = 'grass'
    Bush = 'bush'

class move():
    North = 'moves to the north'
    South = 'moves to the South'
    East = 'moves to the East'
    West = 'moves to the West'

while True:
    for i in range(get_world_size()):
        for i in range(get_world_size()):
            plant(Entities.Bush)
            if can_harvest():
                harvest()
            else:
                break
        move(move.North)
    move(move.East)