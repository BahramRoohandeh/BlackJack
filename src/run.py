from src.utiles import *

os.system('clear')

print('welcome to BLACK JACK\n')



while True:
    d = Deck()
    d.reset()
    d.shuffle()

    player = Hand()
    computer = Hand()

    player.add_card(d.deal())
    player.add_card(d.deal())
    player.adjuster()
    computer.add_card(d.deal())
    computer.add_card(d.deal())
    computer.adjuster()
    counter  = 2
    counter2 = 2

    some_show(player , computer)

    answer = input('hit h or stand s ?')

    while answer not in ['h', 's']:
        print('please insert correct answer')
        answer = input('hit h or stand s ?')

    if answer == 'h':
        while player.cards_value <22 and answer == 'h':

            player.add_card(d.deal())
            print(f'{player.hand[counter].__str__()}')
            print(f' your score : {player.cards_value}')
            print('..................................')
            counter += 1

            if player.cards_value >21:
                print('\n--------YOU LOST------------')
                break
            answer = input('hit h or stand s ?')
            while answer not in ['h', 's']:
                print('please insert correct answer')
                answer = input('hit h or stand s ?')




    if answer == 's':

        show_all(computer)

        while computer.cards_value <22 and computer.cards_value< player.cards_value :


            computer.add_card(d.deal())
            print(f'\n{computer.hand[counter2].__str__()}')


            counter2 += 1
            if computer.cards_value >21:
                print(f'\ndealer score: {computer.cards_value}')
                print('\n--------YOU WON------------')
                break
            if computer.cards_value >player.cards_value:
                break

    if player.cards_value < 22 and computer.cards_value < 22:
        if player.cards_value > computer.cards_value:
            print(f'\ndealer score: {computer.cards_value}')
            print('\n--------YOU WON------------')
        if player.cards_value == computer.cards_value:
            print(f'\ndealer score: {computer.cards_value}')
            print('\n--------EQUAL------------')
        if player.cards_value < computer.cards_value:
            print(f'\ndealer score: {computer.cards_value}')
            print('\n--------YOU LOST------------')


    ans = input('\nDo You Want to Retry ? y/n  ')
    while ans not in ['y', 'n']:
        print('please insert correct answer')
        ans = input('\nDo You Want to Retry ? y/n  ')
    if ans == 'y':
        os.system('clear')
        print('\nwelback to BLACK JACK\n')
        continue
    else:
        break

