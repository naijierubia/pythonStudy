"""
游戏界面
"""
import os

from bll import GameCoreController


class GameConsoleViewer:
    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        for item in range(3):
            self.__controller.add_random_number()
        self.__draw_graphic_interface()

    def __update(self):
        while True:
            if self.__controller.limit_input():
                while True:
                    dir = self.__input('请输入方向:')
                    if self.__controller.row_is_ok() and self.__controller.column_is_ok():
                        break

                    elif self.__controller.row_is_ok() and (not self.__controller.column_is_ok()) \
                            and (dir == 'a' or dir == 'd'):
                        break

                    elif self.__controller.column_is_ok() and (not self.__controller.row_is_ok()) \
                            and (dir == 'w' or dir == 's'):
                        break

                    elif (not self.__controller.column_is_ok()) and (not self.__controller.row_is_ok()):
                        print('游戏结束')
                        raise Exception('game over')

            else:
                dir = self.__input('请输入方向:')
            self.move_location(dir)
            self.__controller.add_random_number()
            self.__draw_graphic_interface()

    def move_location(self, dir):
        if dir == 'w':
            self.__controller.map_transfer_up()
        elif dir == 's':
            self.__controller.map_transfer_down()
        elif dir == 'a':
            self.__controller.map_transfer_left()
        elif dir == 'd':
            self.__controller.map_transfer_right()

    def main(self):
        self.__start()
        self.__update()

    def __draw_graphic_interface(self):
        os.system('cls')
        for row in self.__controller.map:
            for item in row:
                print(item, end='\t')
            print()

    @staticmethod
    def __input(message):
        while True:
            step = input(message)
            if step == 'a' or step == 'w' or step == 's' or step == 'd':
                return step
