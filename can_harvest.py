# increase speed
def harvest():
    print('harvest!')
def can_harvest():
    print('increasing speed')

    while True:
        if can_harvest():
            harvest()
    harvest()