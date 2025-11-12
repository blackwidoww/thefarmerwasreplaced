# can harvest when the plants are fully grown up
def plant():
    print('plant')
def can_harvest():
    print('increasing speed')
def harvest():
    print('harvest!')
class Entities():
    Bush = 'plant a bush'
    Grass = 'plant a grass'
class move():
    North = 'moves to the north'
    South = 'moves to the South'
    East = 'moves to the East'
    West = 'moves to the West'

while True:
    plant(Entities.Bush)
    if can_harvest():
        harvest()
        move(move.North)
harvest()