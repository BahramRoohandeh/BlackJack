from src.funcs import *



os.system('clear')

print('welcome to BLACK JACK\n')


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


some_show(player , computer)


def ask_for_deal(player_ , computer_):
    playing = True
    counter  = 2
    counter2 = 2


    answer = input('hit h or stand s ?')

    while answer not in ['h', 's']:
        print('please insert correct answer')
        answer = input('hit h or stand s ?')

    if answer == 'h':
        while player_.cards_value <22 and answer == 'h':

            player_.add_card(d.deal())
            print(f'{player_.hand[counter].__str__()}')
            print(f' your score : {player_.cards_value}')
            print('..................................')
            counter += 1

            if player_.cards_value >21:
                print('\n--------YOU LOST------------')
                break
            answer = input('hit h or stand s ?')
            while answer not in ['h', 's']:
                print('please insert correct answer')
                answer = input('hit h or stand s ?')




    if answer == 's':

        show_all(computer_)

        while computer_.cards_value <22 and computer_.cards_value< player_.cards_value :


            computer_.add_card(d.deal())
            print(f'\n{computer_.hand[counter2].__str__()}')


            counter2 += 1
            if computer_.cards_value >21:
                print(f'\ndealer score: {computer_.cards_value}')
                print('\n--------YOU WON------------')
                break
            if computer_.cards_value >player_.cards_value:
                break

    if player_.cards_value < 22 and computer_.cards_value < 22:
        if player_.cards_value > computer_.cards_value:
            print('\n--------YOU WON------------')
        if player_.cards_value == computer_.cards_value:
            print('\n--------EQUAL------------')
        if player_.cards_value < computer_.cards_value:
            print(f'\ndealer score: {computer_.cards_value}')
            print('\n--------YOU LOST------------')

    play_again()


def play_again():

    ans = input('\nDo You Want to Retry ? y/n  ')
    while ans not in ['y', 'n']:
        print('please insert correct answer')
        ans = input('\nDo You Want to Retry ? y/n  ')
    if ans == 'y':
        os.system('clear')
        print('\nwelback to BLACK JACK\n')
        d = Deck()
        d.reset()
        d.shuffle()
        player2 = Hand()
        computer2 = Hand()
        player2.add_card(d.deal())
        player2.add_card(d.deal())
        player2.adjuster()
        computer2.add_card(d.deal())
        computer2.add_card(d.deal())
        computer2.adjuster()
        some_show(player2 , computer2)
        ask_for_deal(player2 , computer2)

ask_for_deal(player ,  computer)
