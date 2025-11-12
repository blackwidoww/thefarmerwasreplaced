def harvest():
    print('harvest!')
def do_a_flip():
    print('flip the drone')
class Hats():
    Grey_Hat = 'Grey Hat'
    Purple_Hat = 'Purple Hat'
    Green_Hat = 'Green Hat'
    Brown_Hat = 'Brown Hat'
def change_hat():
    print('change hat color')

    while True:
        harvest()
        change_hat(Hats.Gray_Hat)
        do_a_flip()
        harvest()
        change_hat(Hats.Purple_Hat)
        do_a_flip()
        harvest()
        change_hat(Hats.Green_Hat)
        do_a_flip()
        harvest()
        change_hat(Hats.Brown_Hat)
harvest()

        