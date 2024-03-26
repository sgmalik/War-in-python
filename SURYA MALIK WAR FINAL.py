"""
Surya Malik
sgmalik@uvm.edu
"""


def start_loop():
    while True:
        intro = input('Welcome to War in Python! Are you ready to play? [Y/N]: ')
        intro = intro.upper()
        if intro == 'Y':
            return False
        elif intro == 'N':
            print("I'll let you rethink your answer...")
        elif intro != 'Y' or intro != 'N':
            print('Invalid input, please try again.')


def create_deck():
    suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    return [(suit, value) for suit in suits for value in values]


def shuffle_deck_loop():
    while True:
        shuffle = input('Shuffle deck? [Y/N]: ')
        shuffle = shuffle.upper()
        if shuffle == 'Y':
            random.shuffle(deck)
        elif shuffle == 'N':
            return False
        elif shuffle != 'Y' or shuffle != 'N':
            print('Invalid input, please try again.')


def start_game_loop():
    while True:
        start = input('The deck has been shuffled and distributed, are you ready to begin? [Y/N]: ')
        start = start.upper()
        if start == 'Y':
            print('----------------------------------------------------------------------------')
            return False
        elif start == 'N':
            print("I'll let you rethink your answer...")
        elif start != 'Y' or start != 'N':
            print('Invalid input, please try again.')


def face_card_conversion(card):
    if card == 'Jack':
        return Jack
    elif card == 'Queen':
        return Queen
    elif card == 'King':
        return King
    elif card == 'Ace':
        return Ace
    else:
        return card


def user_wins():
    print('You won this round.')
    user_deck.append(user_card)
    user_deck.append(computer_card)


def computer_wins():
    print('Computer won this round.')
    computer_deck.append(user_card)
    computer_deck.append(computer_card)


def ready_loop():
    while True:
        ready = input('Are you ready for war? [Y/N]: ')
        ready = ready.upper()
        if ready == 'Y':
            return False
        elif ready == 'N':
            print("I'll let you rethink your answer...")
        elif ready != 'Y' or ready != 'N':
            print('Invalid input, please try again.')


def war(user_value_, computer_value_):
    user_war_cards = 0
    computer_war_cards = 0
    while user_value_ == computer_value_:
        print('Uh oh! WAR TIME!!')
        user_deck_length = len(user_deck)
        if user_deck_length == 0:
            print(f'Unfortunately, you have no cards to play for the war now!')
            computer_wins()
            for card in computer_war_list:
                computer_deck.append(card)
            for card in user_war_list:
                computer_deck.append(card)
            return computer_deck
        elif user_deck_length < 4:
            if user_deck_length == 1:
                print(f'You have no cards to play face down for the war.')
                user_war_cards = user_deck.pop(0)
                user_war_list.append(user_war_cards)
                _, user_value_ = user_war_cards
            else:
                for i in range(user_deck_length):
                    user_war_cards = user_deck.pop(0)
                    user_war_list.append(user_war_cards)
                    _, user_value_ = user_war_cards
                if user_deck_length == 2:
                    print(f'You have played 1 cards face down for the war.')
                elif user_deck_length == 3:
                    print(f'You have played 2 cards face down for the war.')
        elif user_deck_length >= 4:
            for i in range(4):
                user_war_cards = user_deck.pop(0)
                user_war_list.append(user_war_cards)
                _, user_value_ = user_war_cards
            print(f'You have played 3 cards face down for the war.')

        computer_deck_length = len(computer_deck)
        if computer_deck_length == 0:
            print(f'Luckily, the computer has no cards to play for the war now!')
            user_wins()
            for card in user_war_list:
                user_deck.append(card)
            for card in computer_war_list:
                user_deck.append(card)
            return user_deck
        if computer_deck_length < 4:
            if computer_deck_length == 1:
                print(f'The computer has no cards to play face down for the war.')
                computer_war_cards = computer_deck.pop(0)
                computer_war_list.append(computer_war_cards)
                _, computer_value_ = computer_war_cards
            else:
                for i in range(computer_deck_length):
                    computer_war_cards = computer_deck.pop(0)
                    computer_war_list.append(computer_war_cards)
                    _, computer_value_ = computer_war_cards
                if computer_deck_length == 2:
                    print(f'The computer has played 1 cards face down for the war.')
                elif computer_deck_length == 3:
                    print(f'The computer has played 2 cards face down for the war.')
        elif computer_deck_length >= 4:
            for i in range(4):
                computer_war_cards = computer_deck.pop(0)
                computer_war_list.append(computer_war_cards)
                _, computer_value_ = computer_war_cards
            print(f'The computer has played 3 cards face down for the war.')

        if user_deck_length < 52 and computer_deck_length < 52:
            ready_loop()
            print(f'Your card: {user_war_cards}')
            print(f'Computer Card: {computer_war_cards}')
            user_value_ = face_card_conversion(user_value_)
            computer_value_ = face_card_conversion(computer_value_)
            if user_value_ > computer_value_:
                user_wins()
                for card in user_war_list:
                    user_deck.append(card)
                for card in computer_war_list:
                    user_deck.append(card)
            elif user_value_ < computer_value_:
                computer_wins()
                for card in computer_war_list:
                    computer_deck.append(card)
                for card in user_war_list:
                    computer_deck.append(card)
    user_war_list.clear()
    computer_war_list.clear()


def create_user_computer_deck():
    s = 0
    for card in deck:
        if s % 2 == 0:
            user_deck.append(card)
            s = 1
        elif s % 2 == 1:
            computer_deck.append(card)
            s = 0


if __name__ == '__main__':

    import random

    start_loop()
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
    print('The rules of the game are as followed: The deck is divided evenly between each player. Each player '
          'receives exactly 26 cards, dealt one at a time, face down. The game begins with each player drawing their '
          'top card and playing it, face up. Whomever has the higher value takes both cards and puts them face down '
          'at the bottom of the stack. This repeats until one player has all 52 cards that were dealt at the start. '
          'The game gets its name when each player draws a card that is the same rank. This is called a war. If this '
          'happens, each player draws another 3 cards, one by one, and places them face down. Finally, a fourth card '
          'is played, face up and whomever has the higher value takes all 10 cards from the round. If a player does '
          'not have enough cards to do a full war, then the last card they have will be played face up to be used in '
          'the war. Good luck and have fun!')

    deck = create_deck()

    random.shuffle(deck)

    print("The deck arrives pre-shuffled however, you are given the option to shuffle the "
          "deck as many times as you'd like.")

    shuffle_deck_loop()

    user_deck = []
    computer_deck = []
    create_user_computer_deck()

    start_game_loop()

    user_deck_length_ = len(user_deck)
    computer_deck_length_ = len(computer_deck)

    user_war_list = []
    computer_war_list = []

    proceed = 'Y'

    print(f'You currently have {user_deck_length_} cards and the computer has {computer_deck_length_}. ')

    counter_loop = True
    counter = 1

    while counter_loop:
        while user_deck_length_ < 52 and computer_deck_length_ < 52:
            user_card = user_deck.pop(0)
            print(f'Your Card: {user_card}')
            computer_card = computer_deck.pop(0)
            print(f'Computer Card: {computer_card}')
            _, user_value = user_card
            _, computer_value = computer_card
            user_value = face_card_conversion(user_value)
            computer_value = face_card_conversion(computer_value)

            if user_value > computer_value:
                user_wins()
            elif user_value < computer_value:
                computer_wins()
            elif user_value == computer_value:
                war(user_value, computer_value)
            user_deck_length_ = len(user_deck)
            computer_deck_length_ = len(computer_deck)

            print(f'You currently have {user_deck_length_} cards and the computer has {computer_deck_length_}. ')

            invalid_input = 0
            if user_deck_length_ == 0 or computer_deck_length_ == 0:
                invalid_input = 2

            while invalid_input < 1:
                cont = input('Would you like to continue to the next round? [Y/N]: ')
                cont = cont.upper()
                if cont == 'Y':
                    print('----------------------------------------------------------------------------')
                    counter_loop = True
                    counter = counter + 1
                    if counter == 1000:
                        print('To save your sanity, the game will be terminated since we have hit 1000 rounds. Go get '
                              'some fresh air!')
                        counter_loop = False
                        break
                    invalid_input = 2
                elif cont == 'N':
                    print('Thank you for playing!')
                    break
                elif cont != 'Y' or cont != 'N':
                    print('Invalid input, please try again.')
            if cont == 'N':
                counter_loop = False
                break

        user_deck_length_ = len(user_deck)
        computer_deck_length_ = len(computer_deck)
        if computer_deck_length_ == 52:
            print('The computer won!')
            counter_loop = False
        elif user_deck_length_ == 52:
            print('You won!')
            counter_loop = False
        elif counter_loop is False:
            print('The game has been terminated')
