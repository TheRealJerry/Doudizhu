order = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','小王','大王']

def convert_combi_to_value(combi):
    global order
    value = []
    for car in combi:
        for ele in order:
            if car == ele:
                value.append(order.index(ele) + 1)
                break
    return value

print(convert_combi_to_value('333'))
# straights
# if value input is lst
def is_straight(prev, value):
    combi = convert_combi_to_value(value)
    p_combi = convert_combi_to_value(prev)
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
    combi = convert_combi_to_value(value)
    p_combi = convert_combi_to_value(prev)
    print(p_combi, combi)
    def helper(value):
        if len(value) != 2 or value[0] != value[1]:
            return False
        return True, value

    res = helper(combi)

    print(res)
    if res != False:
        if p_combi[0] < combi[0]:
            return helper(combi)
        else:
            return False
        
    return res

print(is_pair(['2','2'], ['3','3']))
print(is_pair(['J','J'], ['2','2']))

def is_straight_pair(prev, value):
    combi = convert_combi_to_value(value)
    p_combi = convert_combi_to_value(prev)
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
    combi = convert_combi_to_value(value)
    p_combi = convert_combi_to_value(prev)
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
            
##print(check_3_card('JRRJJ'))
##print(check_3_card('JAJJ'))
##print(check_3_card('26662'))
##

def check_bigger(combi1, combi2):
    global order
    dic1 = {}
    dic2 = {}
    triplet1 = ''
    triplet2 = ''
    check1 = 0
    check2 = 0
    for i in range(len(combi1)):
        if combi1[i] not in dic1:
            dic1[combi1[i]] = 1
        else:
            dic1[combi1[i]] += 1
            
    for j in range(len(combi2)):
        if combi2[j] not in dic2:
            dic2[combi2[j]] = 1
        else:
            dic2[combi2[j]] += 1

    for k in dic1:
        if dic1[k] == 3:
            triplet1 += k

    for z in dic2:
        if dic2[z] == 3:
            triplet2 += z
    for card in range(len(order)):
        if order[card] == triplet1:
            check1 = card
        elif order[card] == triplet2:
            check2 = card
    return check2 > check1

    
##print(is_straight_pair(['2', '2','3', '3','4', '4'], ['1', '1', '2', '2','3', '3']))

