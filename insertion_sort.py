import bisect

def insertion_sort(int_list):
    empty_list = []
    int_list_length = len(int_list)
    while len(empty_list) != len(int_list):
        for i in range(0, len(int_list)):
            bisect.insort(empty_list, int_list[i])
    print(empty_list)

insertion_sort([1, 3, 2, 45, 5])
