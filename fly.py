def fei(curr_lst, prev_lst):
    if curr_lst == None:
        print('due to none')
        return False
    def checker(lst):
        char_lst = []
        ele_counter = []
        for ele in lst:
            if [ele, lst.count(ele)] not in char_lst:
                char_lst.append([ele, lst.count(ele)])
                ele_counter.append(lst.count(ele))
        if len(char_lst) != 4:
            print(char_lst, 1)
            return False
        else:  # feiji check
            if ele_counter.count(3) != 2:
                print(2)
                return False
        three = []  # check if triple1 is > triple2 by 1
        for ele in char_lst:
            if ele[1] == 3:
                three.append(int(ele[0]))
        if min(three) + 1 != max(three):
            print(4)
            return False
        return True, min(three)

    if prev_lst == None:
        return checker(curr_lst)[0]
    else:
        if checker(curr_lst) == False:
            print(5)
            return False
        elif len(curr_lst) != len(prev_lst):
            print('length')
            return False
        else:
            print('end')
            return checker(curr_lst) > checker(prev_lst)


def check_3_card(curr_lst, prev_lst):
    if curr_lst == None:
        return False
    def helper(lst):
        if len(lst) != 5:
            if len(lst) != 4:

                return False
       
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
        final = ''
        for ele in char_lst:
            if ele[1] == 3:
                final = ele[0]
        return True, int(final)
    if prev_lst == None:
        return helper(curr_lst)[0]
    else:
        if helper(prev_lst) == True:
            return False
        elif len(curr_lst) != len(prev_lst):
            return False
        return helper(curr_lst)[1] > helper(prev_lst)[1]

def check_4_card(curr_lst, prev_lst):
    if curr_lst is []:
        print(1)
        return False

    def helper(lst):
        if len(lst) != 6:
            if len(lst) != 8:
                print(2)
                return False

        char_lst = []
        ele_counter = []
        for ele in lst:
            if [ele, lst.count(ele)] not in char_lst:
                char_lst.append([ele, lst.count(ele)])
                ele_counter.append(lst.count(ele))
        if len(char_lst) != 2:
            if len(char_lst) != 3:
                print(3)
                return False
         # feiji check
        if ele_counter.count(4) != 1:
            if ele_counter.count(4) != 2:
                print(4)
                return False
        if len(lst) == 6:
            if ele_counter.count(1) != 2:
                if ele_counter.count(2) != 1 or len(char_lst) != 2:
                    print('issues')
                    return False
        if len(lst) == 8:
            if ele_counter.count(2) != 2:
                if ele_counter.count(4) != 2 or len(char_lst) != 2:
                    print(5)
                    return False
        final = []
        for ele in char_lst:
            if ele[1] == 4:
                final.append(ele[0])
        return True, int(min(final))
    
    if helper(curr_lst) is False:
        return False
    elif prev_lst == []:
        print('run')
        return helper(curr_lst)[0]
    elif helper(prev_lst) is False:
        print(6)
        return False
    elif len(curr_lst) != len(prev_lst):
        print(7)
        return False
    print(8)
    return helper(curr_lst)[1] > helper(prev_lst)[1]
print(check_4_card([12,12,12,12,11,11], []))
