list_merge = [2, 2, 2, 2]
list_map = [
    [2, 0, 0, 2],
    [2, 4, 4, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0],
]


def zero_to_end():
    for item in range(len(list_merge) - 1, -1, -1):
        if list_merge[item] == 0:
            del list_merge[item]
            list_merge.append(0)


def equal_number_add():
    zero_to_end()
    for item in range(len(list_merge) - 1):
        if list_merge[item] == list_merge[item + 1]:
            del list_merge[item + 1]
            list_merge.append(0)
            list_merge[item] *= 2


def map_transfer_left():
    global list_merge
    for item in list_map:
        list_merge = item
        equal_number_add()


def map_transfer_right():
    global list_merge
    global list_map
    for item in list_map:
        i = 0
        list_merge = item[::-1]
        equal_number_add()
        item[::-1] = list_merge


def Square_array_transpose(matrix):
    for x in range(len(matrix)-1):
        for y in range(1, len(matrix)):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]


def map_transfer_up():
    Square_array_transpose(list_map)
    map_transfer_left()
    Square_array_transpose(list_map)


def map_transfer_down():
    Square_array_transpose(list_map)
    map_transfer_right()
    Square_array_transpose(list_map)



