def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Sublist: ", list[start:end + 1])
        steps += 1
        middle = (start + end) // 2
        if list[middle] == element:
            return middle, steps
        elif list[middle] < element:
            start = middle + 1
        else:
            end = middle - 1
    return -1

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

binary_search_result = binary_search(my_list, target)