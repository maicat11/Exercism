from collections import defaultdict

class School(object):
    def __init__(self):
        self.all_students = defaultdict(list)

    def add_student(self, name, grade):
        self.all_students[grade].append(name)

    def roster(self):
        return [st for gr in sorted(self.all_students) for st in sorted(self.all_students[gr])]

    def grade(self, grade_number):
        return sorted(self.all_students[grade_number])
