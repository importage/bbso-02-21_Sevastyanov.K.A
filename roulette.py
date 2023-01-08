import random



def game():
    win = 0
    loose = 0
    while True:
        while True:
            temp_try = int(input('1 - numbers, 2 - red(even), 3 - black(odd)\nType your answer: '))
            if temp_try == 2:
                temp_try = 200
                break
            elif temp_try == 3:
                temp_try == 300
                break
            elif temp_try == 1:
                temp_try = int(input('Enter number(0-36): '))
                if temp_try in range(0, 37):
                    break
            else:
                print('Wrong input. Try Harder!!!')

        ball = random.randint(0, 37)
        print('Выпало: ', ball)
        if temp_try == 200 and ball % 2 == 0 and ball != 0:
            win += 1
            print('You WON!')
        elif temp_try == 300 and ball % 2 == 1:
            print('You WON!')
        elif temp_try == ball:
            win += 1
            print('You WON!')
        else:
            loose += 1
            print('WASTED')

        print(f'wins: {win}\tlooses: {loose}')
        if input('Wanna play again?\ny/n: ').lower() == 'n':
            break



