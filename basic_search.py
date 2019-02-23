def search(int_list, target):
    i = 0
    while (int_list[i] != target):
        i += 1
        if i > (len(int_list)-1):
            return -1

    return i


print(search([8, 32, 109, 202], 202))
