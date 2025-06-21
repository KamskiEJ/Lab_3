class Course:
    def __init__(self, name, description, course_id, teacher):
        self.name = name
        self.description = description
        self.course_id = course_id
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def list_student(self):
        if len(self.students) == 0:
            return "Немає студентів на цьому курсі."

        result = "Список студентів:\n"
        for student in self.students:
            result += student.name + " " + student.last_name + "\n"
        return result
