import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Blackjack:
    def __init__(self):
        return self.cards.pop()

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0

    def deal_initial_cards(self):
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())  
        self.player_hand.append(self.deck.deal_card())  
        self.dealer_hand.append(self.deck.deal_card())  

    def calculate_score(self, hand):
        score = 0
        num_aces = 0
        for card in hand:
            if card.rank == 'Ace':
                score += 11
                num_aces += 1
            elif card.rank in ['King', 'Queen', 'Jack']:
                score += 10
            else:
                score += int(card.rank)

        while score > 21 and num_aces > 0:
            score -= 1 

        return score

    def play(self):
        self.deal_initial_cards()


        print("Player hand:", ', '.join(str(card) for card in self.player_hand))
        print("Dealer hand:", str(self.dealer_hand[0]), "and an unknown card")          

        self.palyer_score = self.calculate_score(self.player_hand)
        self.dealer_score = self.calculate_score(self.dealer_hand)

        while self.player_score < 21:
            action = input("Do you want to hit or stand? (h/s): ").lower()

            if action == 'h':
                self.player_hand.append(self.deck.deal_card())
                self.player_score = self.calculate_score(self.player_hand)
                print("Player hand:", ', '.join(str(card) for card in self.player_hand))

            elif action == 's':
                break
        while self.dealer_score < 17:
            self.dealer_hand.append(self.deck.deal_card())
            self.dealer_score = self.calculate_score(self.dealer_hand)

        print("Player hand:", ', '.join(str(card) for card in self.player_hand))
        print("Player score:", self.player_score)      
        print("Dealer hand:", ', '.join(str(card) for card in self.dealer_hand))      
        print("Dealer score:", self.dealer_score)

        if self.player_score > 21:
            print("Player busts. You lose!")
        elif self.dealer_score > 21:
            print("Dealer busts. You win!")
        elif self.player_score > self.dealer_score:
            print("You win!")
        elif self.player_score < self.dealer_score:
            print("You lose!")
        else:
            print("It's a tie!")

game = Blackjack()
game.play()                                              

# Código do jogo de cartas Blackjack que você joga contra a máquina, onde ela te apresenta suas cartas e você tem que digitar hit or stand (h ou s) para prosseguir ou parar.