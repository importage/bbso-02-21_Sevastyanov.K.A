import bj
import roulette
import rus_roulette


print('Welcome to console Casino!')
while True:
    t = int(input('1 - Roulette, 2 - blackJack, 3 - Russian Rouletter, 4 - quit: '))
    if t == 1:
        roulette.game()
    elif t == 2:
        g = bj.Game()
        g.play()
    elif t == 3:
        rus_roulette.start()
    elif t == 4:
        break
