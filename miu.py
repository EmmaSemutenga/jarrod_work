def is_odd(*array):
    for my_list in array:
        if len(my_list)%2 == 0:
            print(my_list, " its even and no middle number")
        else:
            print((sum(my_list[:(int(len(my_list))/2)])+sum(my_list[(int(len(my_list))/2)+1:])), " its odd")

list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 2, 1, 4, 5]
list_3 = [3, 2, 1, 4, 1]
list_4 = [1, 2, 3, 4]
list_5 = []
list_6 = [10]
mega_list = [list_1, list_2, list_3, list_4, list_5, list_6]
is_odd(*mega_list)
