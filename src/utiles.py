import random
import os


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








