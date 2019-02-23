def selection_sort(int_list):
    empty_list = []
    int_list_length = len(int_list)
    while len(empty_list) != int_list_length:
        min_value = min(int_list)
        empty_list.append(min_value)
        int_list.remove(min_value)
    print(empty_list)

selection_sort([5, 1, 7, 10, 8, 6, 430, 68, 2])
