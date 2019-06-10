STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
PLANT_MAP = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

class Garden(object):
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        self.students = sorted(students) if students else STUDENTS

    def plants(self, name):
        plants = []
        student_idx = self.students.index(name) * 2
        for d in self.diagram:
            plants.append(PLANT_MAP[d[student_idx]])
            plants.append(PLANT_MAP[d[student_idx + 1]])
        return plants