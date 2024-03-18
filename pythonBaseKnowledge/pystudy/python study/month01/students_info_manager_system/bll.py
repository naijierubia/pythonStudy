from model import StudentModel


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

    def load_student_list(self):
        self.add_student(StudentModel('凉宫春日', 16, 98))
        self.add_student(StudentModel('长门有希', 16, 99))
        self.add_student(StudentModel('朝比奈实玖瑠', 17, 94))

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