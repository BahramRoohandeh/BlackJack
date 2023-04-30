import random
import os
os.system('clear')
print('welcome to BLACK JACK')

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
    def __init__(self):
        self.decks = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.decks.append(card)
                
    def __str__(self):
        card_comp = ''
        for deck in self.decks:
            card_name = deck.__str__()
            card_comp += '\n' + card_name
        return 'card list is:' + card_comp 
        
    def shuffle(self):
        return random.shuffle(self.decks)
        
    def deal(self):
        return self.decks.pop()
        
            
    
d = Deck()
d.shuffle()
# card = d.deal()
# print(card)

class Hand():
    def __init__(self):
        # self.first = ''
        self.hand = []
        self.cards_value = 0
        self.aces = 0
    
    def add_card(self, card):
        d1 = d.deal()
        self.hand.append(d1)
        self.cards_value += d1.value
        if d1.rank == 'Ace':
            self.aces += 1
        # self.first += '#'+ d.deal().suit +" "+  d.deal().rank +"#"
        
            
    def adjuster(self):
        while self.cards_value> 21 and self.aces > 0 :
            self.cards_value-= 10
            self.aces -=1
            
    # def __str__(self):
    #     print(self.first)
        
        

player = Hand()
computer = Hand()

player.add_card(d.deal())
player.add_card(d.deal())
player.adjuster()

computer.add_card(d.deal())
computer.add_card(d.deal())
computer.adjuster()

def some_show():
    print('computer hand is :')
    print('1st : ***************')
    print(f'2nd :{computer.hand[1].__str__() }')
    print('------------------------------')
    print('player hand is :')
    print(f'1st :{player.hand[0].__str__() }')
    print(f'2nd :{player.hand[1].__str__() }')
    print(player.cards_value)
    print('------------------------------')
    
    
def show_all():
    for i in range(len(computer.hand)):
        print(f'\n{computer.hand[i].__str__() }')
    
    
    
some_show()    

def ask_for_deal():
    playing = True
    counter  = 2
    counter2 = 2
 
       
    answer = input('hit h or stand s ?')
    if answer == 'h':
        while player.cards_value <22 and answer == 'h':
        
            player.add_card(d.deal())
            print(f'{player.hand[counter].__str__()}')
            print(f' your score : {player.cards_value}')
            print('..................................')
            counter += 1

            if player.cards_value >21:
                print('--------YOU LOST------------')
                break
            answer = input('hit h or stand s ?')
        
        
    if answer == 's':
        
        show_all()

        while computer.cards_value <22 :
        
            
            computer.add_card(d.deal())
            print(f'\n{computer.hand[counter2].__str__()}')
            print(f'\ndealer score: {computer.cards_value}')
            
            counter2 += 1
            if computer.cards_value >21:
                print('--------YOU WON------------')
                break
            if computer.cards_value >18:
                break
        
    if player.cards_value < 22 and computer.cards_value < 22:
        if player.cards_value > computer.cards_value:
            print('--------YOU WON weak------------')
        if player.cards_value == computer.cards_value:
            print('--------EQUAL------------')
        else:
            print('--------YOU LOST weak------------')

    
        
ask_for_deal()
    
    
    
    
    
    
    
    
    
    
    
    