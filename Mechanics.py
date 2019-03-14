import random
from straights import compare

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def __str__(self):
        return self.name

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
        def quicksort(lst):
            if len(lst) <= 1:
                return lst
            else:
                pivot = lst[0]
                small_lst = []
                big_lst = []
                for ele in lst[1:]:
                    if ele.get_value() > pivot.get_value():
                        big_lst.append(ele)
                    else:
                        small_lst.append(ele)
                return quicksort(small_lst) + [pivot,] + quicksort(big_lst)
        self.card = quicksort(self.card)

    def clear_cards(self):
        self.card = []

    def remove_card(self, card_index):
        self.card.pop(card_index)

    def get_card(self):
        return self.card

    def print_card(self):

        for i in range(len(self.card)):
            print(str(self.card[i])+'[{}]'.format(i), end = ' ')

    def set_role(self, boolean):
        self.is_dizhu = boolean

    def get_role(self):
        return self.is_dizhu
    
    def check_winning(self):
        return self.card == []


#  test code
class Game:
    def __init__(self, player1_name, player2_name, player3_name):
        value = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        colour = ['\u2660','\u2663','\u2665','\u2666']
        self.card_set = [Card('大王', 14), Card('小王', 13)]
        self.Player1 = Player(player1_name)
        self.Player2 = Player(player2_name)
        self.Player3 = Player(player3_name)
        self.player_list = [self.Player1, self.Player2, self.Player3]
        self.Dizhu = None
        self.reserved_cards = []
        self.multiplier = 1
        for i in colour:
            for n in value:
                self.card_set.append(Card(i+n, value.index(n)))
    




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

        print('Player 1({}) Cards: '.format(self.Player1.get_name(), end = ''))
        self.Player1.print_card()
        print('\nPlayer 2({}) Cards: '.format(self.Player2.get_name(), end = ''))
        self.Player2.print_card()
        print('\nPlayer 3({}) Cards: '.format(self.Player3.get_name(), end = ''))
        self.Player3.print_card()
            
        print('\nReserved Cards: ', end = '')
        for i in range(3):
            print(self.reserved_cards[i], end = ' ')
        print('\n')




    def auction(self):

        def check_input(user_input):
            if (int(user_input) > previous[1]) or (int(user_input) == 0):
                return True 
            return False

        starter = random.choice(self.player_list)
        self.player_list = self.player_list[self.player_list.index(starter):3]+self.player_list[:self.player_list.index(starter)]

        finished = False

        while not finished:
            for player in self.player_list:
                player.clear_cards()
            self.shuffle()
            self.distribute_cards()
            previous = [None, 0]
            for person in self.player_list:
                done = False
                while not done:
                    user_input = input('{}, Please choose your confidence level from (0, 1, 2, 3): '.format(person.get_name()))
                    done = check_input(user_input)
                if int(user_input) > 0:
                    previous = [person, int(user_input)]
                if int(user_input) == 3:
                    break
            if previous[1] != 0:
                self.Dizhu = previous[0]
                print('{} has become Dizhu!'.format(self.Dizhu.get_name()))
                self.Dizhu.set_role(True)
                for card in self.reserved_cards:
                    self.Dizhu.add_card(card)
                self.Dizhu.rank_cards()
                self.multiplier = previous[1]
                finished = done

        
        # print(self.Player1.get_name(), ('is Dizhu' if self.Player1.get_role() else 'is not Dizhu'))
        # print(self.Player2.get_name(), ('is Dizhu' if self.Player2.get_role() else 'is not Dizhu'))
        # print(self.Player3.get_name(), ('is Dizhu' if self.Player3.get_role() else 'is not Dizhu'))
        # print('Multiplier: ' + str(self.multiplier))


    def play(self):
        def check_input(user_input, player):
            for card_index in user_input:
                if int(card_index) < 0 or int(card_index) >= len(player.get_card()) or user_input.count(card_index) > 1:
                    return False 
            return True
       
       
        previous_card_lst = []
        won = False
        pass_counter = 2
        counter = self.player_list.index(self.Dizhu)
        while not won:
            current_player = self.player_list[counter]
            done = False
            no_card_use = False
            while not done:
                print("\n\n{}'s cards: ".format(current_player.get_name(), end = ''))
                current_player.print_card()
                card_indexes = input("\n{}, please key in the index of the card(s) you want to use (index starts from 0), '-1' if you do not want to use any cards: ".format(current_player.get_name())).split(' ')
                current_card_lst = []
                if card_indexes == ['-1']:
                    if pass_counter < 2:
                        pass_counter += 1
                        done = True
                        no_card_use = True
                else:
                    pass_counter = 0
                    for card_index in card_indexes:
                        current_card_lst.append(current_player.get_card()[int(card_index)])
                    done = (check_input(card_indexes, current_player) and compare(current_card_lst, previous_card_lst))
                if not done:
                    print('\nThe combination of cards is not valid!')
            card_indexes = list(map(lambda x:int(x), card_indexes))
            card_indexes.sort(reverse=True)
            
            print(card_indexes)
            if not no_card_use:
                previous_card_lst = current_card_lst
                for card_index in card_indexes:
                    current_player.remove_card(int(card_index))
            if pass_counter == 2:
                previous_card_lst = []
            print("{}'s cards left: ".format(current_player.get_name(), end = ''))
            current_player.print_card()



            if counter != 2:
                counter += 1
            else:
                counter = 0
            
            won = current_player.check_winning()
       
        print('{} has won!'.format(current_player.get_name()))









game = Game('JR','MK','ZY')
game.auction()
game.play()
