'''value
if (list[value] >= list[value-1]) and (list[value] <= list[value+1])
'''
import bisect

def insertion_sort(int_list):
    empty_list = []
    int_list_length = len(int_list)
    while len(empty_list) != len(int_list):
        for i in range(0, len(int_list)):
            bisect.insort(empty_list, int_list[i])
    print(empty_list)

insertion_sort([1, 3, 2, 45, 5])



'''loop through the list
append first value into empty_list
if the value in front is smaller than the value before it, do bisect() to insert the value in the
right place in empty_list1


[1, 4, 8, 56, 100]
[1, 2, 3, 4 , 5]'''
