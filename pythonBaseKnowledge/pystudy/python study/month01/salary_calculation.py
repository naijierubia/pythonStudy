# class StaffModule:
#     def __init__(self, name='', work='', salary=0, uid=0):
#         self.name = name
#         self.work = work
#         self.salary = salary
#         self.uid = uid
#
#
# class StaffController:
#     uid = 1000
#
#     def __init__(self):
#         self.__list_staff = []
#
#     def add_staff(self, staff):
#         staff.uid = self.uid
#         self.uid += 1
#         self.__list_staff.append(staff.uid)
#
#     def pay_salary(self):

class StaffManager:
    def __init__(self):
        self.__list_staff = []

    def add_staff(self, staff):
        self.__list_staff.append(staff)

    def calculate_salary(self):
        total_salary = 0
        for item in self.__list_staff:
            total_salary += item.get_salary()
        return total_salary


class Staff:
    def __init__(self, bass_salary=0):
        self.bass_salary = bass_salary

    def get_salary(self):
        return self.bass_salary


# ------------------------------------------------------------


class Programmer(Staff):
    def __init__(self, bass_salary=0, bonus_salary=0):
        super().__init__(bass_salary)  # 共性放到父级上
        self.bonus_salary = bonus_salary

    def get_salary(self):
        super().get_salary()
        return super().get_salary() + self.bonus_salary  # base_salary是共性


class Tester(Staff):
    def __init__(self, bass_salary=0, bug_count=0):
        super().__init__(bass_salary)
        self.bug_count = bug_count

    def get_salary(self):
        super().get_salary()
        return super().get_salary() + self.bug_count * 5


manager = StaffManager()
manager.add_staff(Programmer(8000, 2000))
manager.add_staff(Tester(7500, 200))
print(manager.calculate_salary())
