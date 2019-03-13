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
            else:
                continue
        if len(char_lst) != 4:
            print(char_lst, 1)
            return False
        else:  # feiji check
            if ele_counter.count(3) != 2:
                print(2)
                return False
            elif ele_counter.count(2) != 2 and ele_counter.count(1) != 2:
                print(3, ele_counter.count(2), ele_counter.count(1))
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




