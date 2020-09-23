import random
import time
import colorama
from colorama import Fore, Style
playing = True
playername = ' '
chip_mem = 0
zzz = False
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

'''
CLASSES
'''

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
        
    def __str__(self):
        return self.rank + ' of ' + self.suit 


class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
        


class Hand:
  # starter values
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    # keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        pass

class Chips:
    
    def __init__(self):
        self.total = 0
        if chip_mem > 0:
            self.total = chip_mem
        else:
            self.total = 100  # start total 
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        

'''
Definitions
'''


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('\nHi there %s. You currently have %s chips. How many chips will you bet?\n' % (playername, chips.total)))
        except ValueError:
            print('Please Choose a Number\n')
        else:
            if chips.bet > chips.total:
                print("Sorry %s, your bet is higher than your total of" % (playername),chips.total)
            else:
                break  
                
def double_down(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    
    while True:
        x = input("Would you like to Hit, Stand or Double Down? Enter 'h', 's' or 'd'\n")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        
        elif x[0].lower() == 'd':
            print('Double Down. 2x the bet and only 1 more card')
            zzz = True
            hit(deck,hand)
            playing = False

        else:
            print("")
            continue
        break

def show_some(player,dealer):
    print(Fore.RED +'\n______________')
    print(Fore.RED +"Dealer's Hand:")
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    time.sleep(1)
    print(" -- Hidden --")
    print('',dealer.cards[1])
    time.sleep(1)
    print(Fore.BLUE +'\n______________')  
    print(Fore.BLUE +"%s's Hand:" % (playername))
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print(*player.cards, sep='\n ')
    
def show_all(player,dealer):
    print(Fore.RED +'\n______________')
    print(Fore.RED +"Dealer's Hand:")
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print(*dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print(Fore.BLUE +'\n______________')
    print(Fore.BLUE +"%s's Hand:" % (playername))
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print(*player.cards, sep='\n')
    print("%s's Hand =" % (playername),player.value)
    

#game scenarios
def player_busts(player,dealer,chips):
    if zzz == True:
        print('2x Bust')
        chips.lose_bet()
        chips.lose_bet()
     
    else:
        print(Fore.RED +"\n%s busts" % (playername))
        chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print(Fore.GREEN +"\n%s wins" % (playername))
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print(Fore.GREEN +"Dealer busts")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print(Fore.RED +"Dealer wins")
    chips.lose_bet()
    
def push(player,dealer):
    print(Fore.RED +"Tied Game. It's a push.")   


a = ''' 
╔══╗╔╗──────╔╗───╔╗─────╔╗
║╔╗║║║──────║║───║║─────║║
║╚╝╚╣║╔══╦══╣║╔╗─║╠══╦══╣║╔╗
║╔═╗║║║╔╗║╔═╣╚╝╬╗║║╔╗║╔═╣╚╝╝
║╚═╝║╚╣╔╗║╚═╣╔╗╣╚╝║╔╗║╚═╣╔╗╗
╚═══╩═╩╝╚╩══╩╝╚╩══╩╝╚╩══╩╝╚╝'''
  
'''


MAIN GAME CODE STARTS HERE

'''
playername= input('Please enter your name: ')

while True:
    print(Fore.BLUE +a,
    '\n\nRules: Dealer will hit until they reach 17. Aces count as a 1 or 11.\nKing, Queen, and Jack count as 10')

    # create - shuffle - 2 cards each
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # player chips setup
    player_chips = Chips()  
    
    # ask for bet
    take_bet(player_chips)
    
    # show cards, hide 1 dealer 
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # show cards, hide 1 dealer 
        show_some(player_hand,dealer_hand)  
        
        # player bust
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # player no bust - dealer hit until 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # show all cards
        show_all(player_hand,dealer_hand)
        
        # scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # chip toal after game 
    print("\nYour chip total is now",player_chips.total)
    if player_chips.total == 0:
      print('Game Over')
      break

    new_game = input("Play again? Enter 'y' or 'n' \n")
    
    if new_game[0].lower()=='y':
        chip_mem = player_chips.total
        playing=True
        continue
    else:
        break
