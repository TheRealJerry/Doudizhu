def straight(curr_lst, prev_lst):
    def helper(value):
        if len(value) < 5 or int(value[-1]) > 11:    # if last card is bigger than Ace
            return False
        else:
            start = int(value[0])
            for num in value:
                if int(num) != start:
                    return False
                else:
                    start += 1
            return True

    res = helper(curr_lst)
    if res:
        if prev_lst == []:
            return True
        elif helper(prev_lst):
            if prev_lst[0] < curr_lst[0]:
                return True
            else:
                return False
    return False

# test cases
# print(straight(['3','4','5','6','7'], ['1','2','3','4','5'])) # True
# print(straight(['9','10','11','12','13'], ['1','2','3','4','5'])) # False



def pair(curr_lst, prev_lst):
    def helper(value):
        if len(value) != 2 or value[0] != value[1]:
            return False
        return True

    res = helper(curr_lst)
    if res:
        if prev_lst == []:
            return True
        elif helper(prev_lst):
            if prev_lst[0] < curr_lst[0]:
                return True
            else:
                return False
    return False

# test cases
# print(pair(['2','2'], ['3','3'])) # False
# print(pair(['9','9'], ['2','2'])) # True




def straight_pair(curr_lst, prev_lst):
    def helper1(value):     # check whether the input list only comprises pairs of cards
        if len(curr_lst) < 6 or int(curr_lst[-1]) > 11 or len(curr_lst) % 2 != 0:
            return False
        for i in curr_lst:
            if curr_lst.count(i) != 2:
                return False
        return True

    def helper2(value, prev):     # validate whether the pairs are in increasing order
        if len(value) == 0:
            return True
        else:
            temp_pair = value[:2]
            if pair(temp_pair, prev) and int(temp_pair[0]) == int(prev[0])+1:
                return helper2(value[2:], temp_pair)
            else:
                return False

    if helper1(curr_lst):
        res = helper2(curr_lst, [str(int(curr_lst[0])-1), str(int(curr_lst[0])-1)])
        if res:
            if prev_lst == []:
                return True
            elif helper2(prev_lst, [str(int(prev_lst[0])-1), str(int(prev_lst[0])-1)]):
                if prev_lst[0] < curr_lst[0] and len(prev_lst) == len(curr_lst):
                    return True
        return False

    return False

# test cases
# print(straight_pair(['3','3','4','4','5','5','6','6'],['7','7','8','8','9','9','10','10'])) # False
# print(straight_pair(['3','3','4','4','5','5','6','6'],['1','1','2','2','3','3','4','4'])) # True
# print(straight_pair(['3','3','4','4','5','5','6','6'],['1','1','2','2','3','4','4','4'])) # False
# print(straight_pair(['3','3','4','4','5','5','6','6'],['1','1','2','2','3','3'])) # False
# print(straight_pair(['3','3','4','4','5','5','6','6'],['0','0','1','1','2','2','3','3'])) # True
# print(straight_pair(['3','3','4','4','5','5','6','6'],[])) # True



def single_card(curr_lst, prev_lst):
    if len(curr_lst) == 1:
        if prev_lst == []:
            return True
        elif len(prev_lst) == 1:
            return int(prev_lst[0]) < int(curr_lst[0])
    return False

# test case
# print(single_card(['12'], ['2'])) # True
# print(single_card(['1'], ['3'])) # False



def bomb(curr_lst, prev_list):
    if len(curr_lst) == 4 and curr_lst.count(curr_lst[0]) == 4:
        if prev_list == []:
            return True
        elif len(prev_list) == 4 and prev_list.count(prev_list[0]) == 4:
            if int(curr_lst[0]) > int(prev_list[0]):
                return True
            return False
        else:
            if prev_list == ['13', '14']:
                return False
            return True

# test case
print(bomb(['4','4','4','4'], ['5','5','5','5'])) # False
print(bomb(['6','6','6','6'], ['3','3','3','3'])) # True
print(bomb(['8','8','8','8'], ['13', '14'])) # False




def compare(curr_list, prev_list):
    current_list = []
    previous_list = []
    for ele in curr_list:
        current_list.append(ele.get_value())
        current_list.sort()
    for ele in prev_list:
        previous_list.append(ele.get_value())
        previous_list.sort()



    if len(current_list) == 2 and int(current_list[0]) > 12 and int(current_list[1]) > 12:     # Check Rocket
        return True

    else:
        return straight(current_list, previous_list) or pair(current_list, previous_list) or straight_pair(current_list, previous_list) \
            or single_card(current_list, previous_list)


def fei(curr_lst, prev_lst):
    if curr_lst == None:
  
        return False
    def checker(lst):
        char_lst = []
        ele_counter = []
        for ele in lst:
            if [ele, lst.count(ele)] not in char_lst:
                char_lst.append([ele, lst.count(ele)])
                ele_counter.append(lst.count(ele))
        if len(char_lst) != 4:

            return False
        else:  # feiji check
            if ele_counter.count(3) != 2:

                return False
        three = []  # check if triple1 is > triple2 by 1
        for ele in char_lst:
            if ele[1] == 3:
                three.append(int(ele[0]))
        if min(three) + 1 != max(three):

            return False
        return True, min(three)

    if prev_lst == None:
        return checker(curr_lst)[0]
    else:
        if checker(curr_lst) == False:

            return False
        elif len(curr_lst) != len(prev_lst):

            return False
        else:

            return checker(curr_lst) > checker(prev_lst)


def check_3_card(curr_lst, prev_lst):
    if curr_lst == None:
        return False
    def helper(lst):
        if len(lst) != 5:
            if len(lst) != 4:

                return False
        else:
            char_lst = []
            ele_counter = []
            for ele in lst:
                if [ele, lst.count(ele)] not in char_lst:
                    char_lst.append([ele, lst.count(ele)])
                    ele_counter.append(lst.count(ele))
            if len(char_lst) != 2:

                return False
            else:  # feiji check
                if ele_counter.count(3) != 1:

                    return False
        return True, int(min(lst))
    if prev_lst == None:
        return helper(curr_lst)[0]
    else:
        if helper(prev_lst) == True:
            return False
        elif len(curr_lst) != len(prev_lst):
            return False
        return helper(curr_lst)[1] > helper(prev_lst)[1]
