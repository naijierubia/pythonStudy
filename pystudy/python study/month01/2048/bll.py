"""
游戏核心控制器
"""
import random

from module import LocationModule


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__none_map = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for item in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[item] == 0:
                del self.__list_merge[item]
                self.__list_merge.append(0)

    def __equal_number_add(self):
        self.__zero_to_end()
        for item in range(len(self.__list_merge) - 1):
            if self.__list_merge[item] == self.__list_merge[item + 1]:
                del self.__list_merge[item + 1]
                self.__list_merge.append(0)
                self.__list_merge[item] *= 2

    def map_transfer_left(self):
        for item in self.__map:
            self.__list_merge = item
            self.__equal_number_add()

    def map_transfer_right(self):
        for item in self.__map:
            self.__list_merge = item[::-1]
            self.__equal_number_add()
            item[::-1] = self.__list_merge

    def __Square_matrix_transpose(self):
        for x in range(len(self.__map) - 1):
            for y in range(x + 1, len(self.__map)):
                self.__map[x][y], self.__map[y][x] = self.__map[y][x], self.__map[x][y]

    def map_transfer_up(self):
        self.__Square_matrix_transpose()
        self.map_transfer_left()
        self.__Square_matrix_transpose()

    def map_transfer_down(self):
        self.__Square_matrix_transpose()
        self.map_transfer_right()
        self.__Square_matrix_transpose()

    def add_random_number(self):
        self.__find_none_position()
        number = self.__random_generate()
        position = self.__select_none_position()
        """
        random中提供了choice方法来随机返回可迭代对象中的元素
        """
        self.__map[position.row][position.column] = number

    def __find_none_position(self):
        self.__none_map.clear()
        for row in range(len(self.__map)):
            for column in range(len(self.__map[row])):
                if self.__map[row][column] == 0:
                    self.__none_map.append(LocationModule(row, column))

    @staticmethod
    def __random_generate():
        a = random.randint(1, 10)
        if a > 9:
            return 4
        else:
            return 2

    def __select_none_position(self):
        if len(self.__none_map):
            a = random.randint(0, len(self.__none_map) - 1)
            return self.__none_map[a]

    def is_game_over(self):
        if len(self.__none_map) > 0:
            return False

        for row in range(len(self.__map)):
            for column in range(len(self.__map) - 1):
                if self.__map[row][column] == self.__map[row][column + 1] and \
                        self.__map[column][row] == self.__map[column + 1][row]:
                    return False
        return True

        # for column in range(len(self.__map)):
        #     for row in range(len(self.__map)-1):
        #         if self.__map[column][row] == self.__map[column + 1][row]:
        #             return False

    def limit_input(self):
        for row in self.__map:
            for item in row:
                if item == 0:
                    return False
        return True

    def row_is_ok(self):
        for row in range(len(self.__map)):
            for column in range(len(self.__map) - 1):
                if self.__map[row][column] == self.__map[row][column + 1]:
                    return True
        return False

    def column_is_ok(self):
        for column in range(len(self.__map)):
            for row in range(len(self.__map) - 1):
                if self.__map[row][column] == self.__map[row + 1][column]:
                    return True
        return False


if __name__ == '__main__':
    controller = GameCoreController()
    controller.map_transfer_down()
    print(controller.map)
    controller.add_random_number()
    print(controller.map)
