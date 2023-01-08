import random

def start():
    lvl = int(input('Choose ur difficulty level(1-6)\n'
                    'Выберите уровень сложности(1-6): '))

    barrel = [1, 2, 3, 4, 5, 6]
    loaded_barrel = []
    for i in range(lvl):
        temp = random.choice(barrel)
        loaded_barrel.append(temp)
        barrel.remove(temp)

    print('Spin da WHEEl!'
          'Крутите барабан! ')
    while True:
        temp = int(input('1 - крутить барабан(Spin da WHEEEEEL!\n'
                         '2 - Крутить больше некому(WASTED)\n'))
        if temp == 1:
            destiny = random.randint(1, 6)
            if destiny in barrel:
                print('ALIVE!\n'
                      'КАК ЗАНОВО РОДИЛСЯ')
            else:
                print('WASTED\n'
                      'Кто ж знал...')
        else:
            break
