def harvest():
    print('harvest')

def clear():
    clear = 'clear'

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

clear()
while True:
	for i in range(3):
		for j in range(3):
			if can_harvest():
				harvest()
				till()
				plant(Entities.Carrot)
				move(move.North)
			else:
				do_a_flip()
				move(move.East)