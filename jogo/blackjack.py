# Embaralhas cartas
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)


class Hand:  # Mao(Conjunto de cartas)
    def __init__(self):  # Inicia zerada
        self.cards = list()
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ''
        for card in self.cards:  # cada carta existente na mao sera adicionada no hand_comp
            card_name = card.__str__()
            hand_comp += ' ' + card_name
        return f'Te hand has {hand_comp}'

    def card_add(self, card):  # adiciona cartas na mao do usuario
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):  # Calcurar valor da mao
        if self.ace == True and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


class Deck:  # barralho
    def __init__(self):
        self.deck = list()
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):  # baralhar
        random.shuffle(self.deck)

    def deal(self):  # da uma carta
        sinlge_card = self.deck.pop()
        return sinlge_card

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += ' ' + card.__str__()
            return f'The deck has {deck_comp}'


def make_bet():  # fazer aposta
    global bet
    bet = 0
    print('What amount of chips you like to bet? (Enter whole integer please)')

    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if 1 < bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print(f'Invalid bet. You have only {chip_pool} chips reamining: ')


def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()  # Pega baralho
    deck.shuffle()  # Baralha o deck

    make_bet()  # Usuario faz a aposta

    player_hand = Hand()
    dealer_hand = Hand()

    # 2 cartas para o jogador
    player_hand.card_add(deck.deal())  # da uma carta ao usuario
    player_hand.card_add(deck.deal())  # da uma carta ao usuario

    # 2 cartas para o dealer
    dealer_hand.card_add(deck.deal())  # da uma carta o dealer
    dealer_hand.card_add(deck.deal())  # da uma carta o dealer

    result = 'Hit or Stand? Predd "h" or "s"'

    playing = True
    game_step()


def hit():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing:
        if player_hand.calc_val() <= 21:  # adiciona carta se o valor total das cartas do usuario for menor  ou igual a 21
            player_hand.card_add(deck.deal())
        print(f'Player hand is {player_hand}')

        if player_hand.calc_val() > 21:
            result = 'Busted!' + restar_phrase
            chip_pool -= bet
            playing = False
    else:
        result = "Sorry, can't hit" + restar_phrase

    game_step()


def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if not playing:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"
    else:
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_val() > 21:
            result = f"Dealer bust! You win!{restar_phrase}"
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = "You bet dealer! You win!" + restar_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = "Tied up!" + restar_phrase
            playing = False
        else:
            result = 'Dealer win!' + restar_phrase
            chip_pool -= bet
            playing = False
    game_step()


def game_step():
    print()
    print('Player hand is: ')
    player_hand.draw(hidden=False)
    print(f'Player hand total is {str(player_hand.calc_val())}')

    print()
    print('Dealer hand is: ')
    player_hand.draw(hidden=True)
    print(f'Dealer hand total is {str(dealer_hand.calc_val())}')

    if not playing:
        print(f'Chip total: {str(chip_pool)}')

    print(result)

    player_input()


def game_exit():
    print('Tanks you for playing!')
    exit()


def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print('Invalid input... Enter h, s, d or q: ')
        player_input()


playing = False
chip_pool = 100
bet = 1
restar_phrase = 'Press "d" to shuffle again or press "q" to leave'

suits = ('H', 'D', 'C', 'S')  # tipos d carta: H = Coraca-, D = Diamante/Ouro, C = arroz/trevo S = espada
ranking = ('a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k')
card_val = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10,
            'k': 10}  # Valor da carta

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

deal_cards()
