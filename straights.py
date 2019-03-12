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
    if res and helper(prev_lst):
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
    if res and helper(prev_lst):
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
        if res and helper2(prev_lst, [str(int(prev_lst[0])-1), str(int(prev_lst[0])-1)]):
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



def single_card(curr_lst, prev_lst):
    if len(prev_lst) == len(curr_lst) == 1:
        return int(prev_lst[0]) < int(curr_lst[0])
    return False

# test case
# print(single_card(['12'], ['2'])) # True
# print(single_card(['1'], ['3'])) # False





def compare(curr_list, prev_list):
    current_list = []
    previous_list = []
    if prev_list == []:
        return True
    for ele in curr_list:
        current_list.append(ele.get_value())
        current_list.sort()
    for ele in prev_list:
        previous_list.append(ele.get_value())
        previous_list.sort()


    if len(current_list) == 4 and current_list.count(current_list[0]) == 4:     # Check Bomb
        if len(previous_list) == 4 and previous_list.count(previous_list[0]) == 4:
            if int(current_list[0]) > int(previous_list[0]):
                return True
            return False
        else:
            if previous_list == ['13', '14']:
                return False
            return True

    elif len(current_list) == 2 and int(current_list[0]) > 12 and int(current_list[1]) > 12:     # Check Rocket
        return True

    else:
        return straight(current_list, previous_list) or pair(current_list, previous_list) or straight_pair(current_list, previous_list) \
            or single_card(current_list, previous_list)


























# def check_3_card(combi):
#     count1 = 0
#     count2 = 0
#     lst = []
#     check = True
#     if len(combi) == 4:
#         for i in combi:
#             if i not in lst:
#                 lst.append(i)
#             else:
#                 if i  == lst[0]:
#                     count1 += 1
#                 elif i == lst[1]:
#                     count2 +=1
#         if count1 == 1 or count2 == 1:
#             check = False
#     elif len(combi) == 5:
#         for i in combi:
#             if i not in lst:
#                 lst.append(i)
#             else:
#                 if i  == lst[0]:
#                     count1 += 1
#                 elif i == lst[1]:
#                     count2 +=1
#         if count1 + count2 != 3 and len(lst) != 2 and count1 == 0 or count2 == 0:
#             check = False
#     else:
#         check = False

#     return check
            


# def check_bigger(prev, curr): #  for triplets
#     max_prev = max(prev,key=prev.count)
#     max_curr = max(curr,key=curr.count)
#     return max_prev < max_curr

# #print(check_bigger(['1', '1', '1', '2', '2'], ['3', '3', '3', '4', '4']))
# ##print(is_straight_pair(['2', '2','3', '3','4', '4'], ['1', '1', '2', '2','3', '3']))