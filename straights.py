def compare(curr_list, prev_list):
    current_list = []
    previous_list = []
    if prev_list = None:
        return True
    for ele in curr_list:
        current_list.append(ele.get_value())
    for ele in prev_list:
        previous_list.append(ele.get_value())
    if len(current_list) == 4 and current_list.count(current_list[0]) == 4:
        if len(previous_list) == 4 and previous_list.count(previous_list[0]) == 4:
            if current_list[0] > previous_list[0]:
                return True
            return False
        return True

    elif len(current_list) == 2 and current_list[0].get_value() > 12 and current_list[1].get_value() > 12:
        return True
    
    elif check_3_card(current_list):
        if check_3_card(previous_list):
            return check_bigger(previous_list, current_list)
        return False

    else:
        return is_straight(previous_list, current_list) or is_pair(previous_list, current_list) \
            or is_straight_pair(previous_list, current_list) or is_bigger(previous_list, current_list)











# straights
# if value input is lst
def is_straight(prev, value):
    combi = value
    p_combi = prev
    def helper(value):
        if len(value) < 5 or int(value[-1]) > 12:    # if last card is bigger than Ace
            return False
        else:
            start = int(value[0]) # in case value in lst is str
            for num in value:
                if int(num) != start:
                    return False
                else:
                    start += 1
            return True , value
    res = helper(combi)
    if res != False:
        if p_combi[0] < combi[0]:
            return helper(combi)
        else:
            return False
        
    return res

def is_pair(prev, value):
    combi = value
    p_combi = prev
    def helper(value):
        if len(value) != 2 or value[0] != value[1]:
            return False
        return True, value

    res = helper(combi)
    if res != False:
        if p_combi[0] < combi[0]:
            return helper(combi)
        else:
            return False
        
    return res

##print(is_pair(['2','2'], ['3','3']))
##print(is_pair(['J','J'], ['2','2']))

def is_straight_pair(prev, value):
    combi = value
    p_combi = prev
    if len(combi) < 6 or int(combi[-1]) > 12 or len(combi) % 2 != 0:
        return False
    else:
        def helper(value):
            if len(value) == 0:
                return True
            else:
                pair = value[:2]
                if is_pair(['0'], pair):
                    return helper(value[2:])
                else:
                    return False
        
        res = helper(combi)

        if res != False:
            if p_combi[0] < combi[0]:
                return helper(combi)
            else:
                return False
        
        return res    
     
def is_bigger(prev_val, curr_val):
    combi = value
    p_combi = prev
    return int(p_combi) < int(combi)

def check_3_card(combi):
    count1 = 0
    count2 = 0
    lst = []
    check = True
    if len(combi) == 4:
        for i in combi:
            if i not in lst:
                lst.append(i)
            else:
                if i  == lst[0]:
                    count1 += 1
                elif i == lst[1]:
                    count2 +=1
        if count1 == 1 or count2 == 1:
            check = False
    elif len(combi) == 5:
        for i in combi:
            if i not in lst:
                lst.append(i)
            else:
                if i  == lst[0]:
                    count1 += 1
                elif i == lst[1]:
                    count2 +=1
        if count1 + count2 != 3 and len(lst) != 2 and count1 == 0 or count2 == 0:
            check = False
    else:
        check = False

    return check
            


def check_bigger(prev, curr): #  for triplets
    max_prev = max(prev,key=prev.count)
    max_curr = max(curr,key=curr.count)
    return max_prev < max_curr

#print(check_bigger(['1', '1', '1', '2', '2'], ['3', '3', '3', '4', '4']))
##print(is_straight_pair(['2', '2','3', '3','4', '4'], ['1', '1', '2', '2','3', '3']))

