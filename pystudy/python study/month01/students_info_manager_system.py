# MVC架构model、view、control
# 需要对数据进行唯一表示，将来有g_uid全球唯一标识符

class StudentModel:
    def __init__(self, name='', age=0, score=0, uid=0):
        self.name = name
        self.age = age
        self.score = score
        self.uid = uid


class StudentManagerController:
    init_uid = 1000

    @classmethod
    def __generate_uid(cls, stu):
        stu.uid = cls.init_uid
        cls.init_uid += 1

    def find_student_by_uid(self, stu_uid):
        for item in self.__stu_list:
            if item.uid == stu_uid:
                return item
        return False

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        StudentManagerController.__generate_uid(stu)
        self.__stu_list.append(stu)

    def remove_student(self, stu_uid):
        stu_pos = self.find_student_by_uid(stu_uid)
        print(stu_pos.name, '已被删除')
        self.__stu_list.remove(stu_pos)

    def update_student_info(self, stu_uid, stu_name='', stu_age=0, stu_score=0):
        stu_pos = self.find_student_by_uid(stu_uid)
        if stu_name:
            stu_pos.name = stu_name
        if stu_age:
            stu_pos.age = stu_age
        if stu_score:
            stu_pos.score = stu_score

    def sort_raise_by_score(self):
        for x in range(len(self.__stu_list) - 1):
            for y in range(x + 1, len(self.__stu_list)):
                if self.__stu_list[x].score > self.__stu_list[y].score:
                    self.__stu_list[x], self.__stu_list[y] = self.__stu_list[y], self.__stu_list[x]

    def sort_down_by_score(self):
        self.sort_raise_by_score()
        self.__stu_list.reverse()

    def sort_raise_by_age(self):
        for x in range(len(self.__stu_list) - 1):
            for y in range(x + 1, len(self.__stu_list)):
                if self.__stu_list[x].age > self.__stu_list[y].age:
                    self.__stu_list[x], self.__stu_list[y] = self.__stu_list[y], self.__stu_list[x]

    def sort_down_by_age(self):
        self.sort_raise_by_age()
        self.__stu_list.reverse()


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
        StudentManagerViewer.selection = int(input('请输入选项:'))
        return StudentManagerViewer.selection

    def __select_menu(self):
        item = StudentManagerViewer.__init_selection()

        if item == 1:
            self.__intput_student()

        elif item == 2:
            self.__display_student_info()
        elif item == 3:
            self.__delete_student()
        elif item == 4:
            self.__update_studnet_info()
        elif item == 5:
            self.__controller.sort_raise_by_score()
            print('已经按照成绩升序排列')
        elif item == 6:
            self.__controller.sort_down_by_score()
            print('已经按照成绩降序排列')

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
            if StudentManagerViewer.selection == 7:
                break

    def __intput_student(self):
        name = input('请输入学生姓名:')
        age = int(input('请输入学生年龄:'))
        score = int(input('请输入学生分数:'))
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)

    def __display_student_info(self):
        tplt = "{0:^8}\t{1:^10}\t{2:^8}\t{3:^8}"
        print(tplt.format('学生编号', '学生姓名', '学生年龄', '学生分数', chr(12288)))
        for item in self.__controller.stu_list:
            print(tplt.format(item.uid, item.name, item.age, item.score, chr(12288)))

    def __delete_student(self):
        stu_uid = int(input('请输入要删除的学生的uid:'))
        if self.__controller.find_student_by_uid(stu_uid):
            self.__controller.remove_student(stu_uid)
        else:
            print('该学生不存在')

    def __update_studnet_info(self):
        stu_uid = int(input('请输入学生的uid:'))
        if self.__controller.find_student_by_uid(stu_uid):
            print('如果无需修改则不输入')
            stu_name = input('请修改学生的姓名:')
            stu_age = int(input('请输入学生的年龄:'))
            stu_score = int(input('请输入学生的分数:'))
            self.__controller.update_student_info(stu_uid, stu_name, stu_age, stu_score)

        else:
            print('该学生不存在')


view = StudentManagerViewer()
view.main()