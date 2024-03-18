from bll import StudentManagerController
from model import StudentModel


class StudentManagerViewer:
    selection = 0

    def __init__(self):
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print('1)添加学生信息')
        print('2)显示学生信息')
        print('3)删除学生信息')
        print('4)修改学生信息')
        print('5)根据程序升序排列')
        print('6)根据程序降序排列')
        print('7)离开')

    @classmethod
    def __init_selection(cls):
        cls.selection = cls.__int__input('请输入选项:')
        return cls.selection

    def __select_menu(self):
        item = StudentManagerViewer.__init_selection()

        if item == 1:
            self.__input_student()

        elif item == 2:
            self.__display_student_info()
        elif item == 3:
            self.__delete_student()
        elif item == 4:
            self.__update_student_info()
        elif item == 5:
            self.__controller.sort_raise_by_score()
            print('已经按照成绩升序排列')
        elif item == 6:
            self.__controller.sort_down_by_score()
            print('已经按照成绩降序排列')

    def main(self):
        self.__controller.load_student_list()
        while True:
            self.__display_menu()
            self.__select_menu()
            if StudentManagerViewer.selection == 7:
                break

    def __input_student(self):
        name = input('请输入学生姓名:')
        age = self.__int__input('请输入学生的年龄:')
        score = self.__int__input('请输入学生分数:')
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __display_student_info(self):
        tplt = "{0:^8}\t{1:^10}\t{2:^8}\t{3:^8}"
        print(tplt.format('学生编号', '学生姓名', '学生年龄', '学生分数', chr(12288)))
        for item in self.__controller.stu_list:
            print(tplt.format(item.uid, item.name, item.age, item.score, chr(12288)))

    def __delete_student(self):
        stu_uid = self.__int__input('请输入要删除的学生的uid:')
        if self.__controller.find_student_by_uid(stu_uid):
            self.__controller.remove_student(stu_uid)
        else:
            print('该学生不存在')

    def __update_student_info(self):
        stu_uid = self.__int__input('请输入学生的uid:')
        if self.__controller.find_student_by_uid(stu_uid):
            print('如果无需修改则不输入')
            stu_name = input('请修改学生的姓名:')
            stu_age = self.__int__input('请输入年龄:')
            stu_score = self.__int__input('请输入学生的分数:')
            self.__controller.update_student_info(stu_uid, stu_name, stu_age, stu_score)

        else:
            print('该学生不存在')

    @staticmethod
    def __int__input(message):
        while True:
            try:
                return int(input(message))
            except:
                print('输入有误')
