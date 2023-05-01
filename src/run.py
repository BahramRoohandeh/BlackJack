import random
import os
os.system('clear')

print('welcome to BLACK JACK\n')

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks =('Four', 'Five', 'Six', 'Seven','Eight','Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,'Jack':2, 'Queen':3, 'King':4, 'Ace':11}


class Card:
    def __init__(self, rank,suit):
        self.suit = suit
        self.rank = rank
        self.value= values[rank]

    def __str__(self):
        return self.rank +' of '  + self.suit



class Deck:
    def reset(self):
        self.decks = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.decks.append(card)

    def shuffle(self):
        return random.shuffle(self.decks)

    def deal(self):
        return self.decks.pop()


d = Deck()
d.reset()
d.shuffle()


class Hand():

    def __init__(self):
        self.hand = []
        self.cards_value = 0
        self.aces = 0


    def add_card(self , input):
        self.hand.append( input)
        self.cards_value += input.value
        if   input.rank == 'Ace':
            self.aces += 1


    def adjuster(self):
        while self.cards_value> 21 and self.aces > 0 :
            self.cards_value-= 10
            self.aces -=1


player = Hand()
computer = Hand()

player.add_card(d.deal())
player.add_card(d.deal())
player.adjuster()
computer.add_card(d.deal())
computer.add_card(d.deal())
computer.adjuster()


def some_show(player_ , computer_):
    print('computer hand is :')
    print('1st : ***************')
    print(f'2nd :{computer_.hand[1].__str__() }')
    print('------------------------------')
    print('player hand is :')
    print(f'1st :{player_.hand[0].__str__() }')
    print(f'2nd :{player_.hand[1].__str__() }')
    print(player_.cards_value)
    print('------------------------------')


def show_all(computer_):
    for i in range(len(computer_.hand)):
        print(f'\n{computer_.hand[i].__str__() }')


some_show(player , computer)

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


ask_for_deal(player ,  computer)

