class Students():

    student_id = 1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = Students.student_id

        Students.student_id += 1
