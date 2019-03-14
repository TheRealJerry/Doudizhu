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
                print('len issues')
                return False
        else:
            char_lst = []
            ele_counter = []
            for ele in lst:
                if [ele, lst.count(ele)] not in char_lst:
                    char_lst.append([ele, lst.count(ele)])
                    ele_counter.append(lst.count(ele))
            if len(char_lst) != 2:
                print('not only 2 ele')
                return False
            else:  # feiji check
                if ele_counter.count(3) != 1:
                    print('ele issue')
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
