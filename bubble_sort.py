def bubble_sort(int_list):
    for i in range(0, len(int_list)):
        if (i == 0):
            pass
        elif int_list[i] < int_list[i-1]:
            int_list[i], int_list[i-1] = int_list[i-1], int_list[i]
            print('lol')
        print(int_list)

    print(int_list)
