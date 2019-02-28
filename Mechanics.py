import random

class Player:
    def __init__(self, name):
        self.name = name
        self.card = []
        self.is_dizhu = False

    def get_name(self):
        return self.name

    def add_card(self, card):
        self.card.append(card)
    
    def rank_cards(self):
        self.card.sort()
        order = ['34567891JQKA2小大'.index(r[1] if r[1] != '王' else r[0]) for r in self.card]
        temp_dict = dict((self.card[i], order[i]) for i in range(17))
        self.card = list(map(lambda pair: pair[0], sorted(temp_dict.items(), key=lambda x: x[1])))

    def remove_card(self, card):
        self.card.remove(card)

    def get_card(self):
        return self.card

    def set_role(self, boolean):
        self.is_dizhu = boolean

    def get_role(self):
        return self.is_dizhu
    
# class Card:
#     def __init__(self, name, value):
#         self.colour = colour
#         self.value = value
    
#     def __str__(self):
#         return self.colour + self.value

class Game:
    def __init__(self, player1_name, player2_name, player3_name):
        value = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        colour = ['\u2660','\u2663','\u2665','\u2666']
        self.card_set = ['大王','小王']
        self.Player1 = Player(player1_name)
        self.Player2 = Player(player2_name)
        self.Player3 = Player(player3_name)
        self.reserved_cards = []
        self.multiplier = 1
        for i in colour:
            for n in value:
                self.card_set.append(i+n)
    
    def shuffle(self):
        random.shuffle(self.card_set)
    
    def distribute_cards(self):
        self.reserved_cards = self.card_set[-3:]
        for i in range(0,51,3):
            self.Player1.add_card(self.card_set[i])
            self.Player2.add_card(self.card_set[i+1])
            self.Player3.add_card(self.card_set[i+2])

        self.Player1.rank_cards()
        self.Player2.rank_cards()
        self.Player3.rank_cards()
        print(self.Player1.get_card())
        print(self.Player2.get_card())
        print(self.Player3.get_card())
        print(self.reserved_cards)

    def auction(self):
        def check_input(user_input):
            if (int(user_input) > previous[1]) or (int(user_input) == 0):
                return True 
            return False

        player_list = [self.Player1, self.Player2, self.Player3]
        random.shuffle(player_list)
        for player in player_list:
            print(player.get_name())
        previous = [None, 0]
        for person in player_list:
            done = False
            while not done:
                user_input = input('Please choose your confidence level from (0, 1, 2, 3): ')
                done = check_input(user_input)
            previous = [person, int(user_input)]
            if int(user_input) == 3:
                break
        if previous[1] != 0:
            previous[0].set_role(True)
            self.multiplier = previous[1]
        else:
            self.shuffle()
            self.distribute_cards()
            self.auction()

        print(self.Player1.get_role())
        print(self.Player2.get_role())
        print(self.Player3.get_role())
        print(self.multiplier)


game = Game('MK','JR','ZY')
game.shuffle()
game.distribute_cards()
game.auction()
