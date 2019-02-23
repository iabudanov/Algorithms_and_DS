def binary_search(int_list, target):
    start_index = 0
    end_index = len(int_list)-1
    pivot_index = (start_index + end_index)//2

    while True:
        if target == int_list[pivot_index]:
            return pivot_index

        if target < int_list[pivot_index]:
            end_index = pivot_index - 1
            pivot_index = (start_index + end_index)//2

        if target > int_list[pivot_index]:
            start_index = pivot_index + 1
            pivot_index = (start_index + end_index)//2

        if start_index > end_index:
            return None

print(binary_search([1, 2, 5, 8, 90, 123, 145], 146))