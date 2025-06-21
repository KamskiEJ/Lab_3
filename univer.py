import pickle

class University:
    def __init__(self, name):
        self.name = name
        self.list_students = []
        self.list_teachers =[]
        self.list_courses = []

    def add_student(self, student):
        self.list_students.append(student)

    def add_teacher(self, teacher):
        self.list_teachers.append(teacher)

    def add_course(self, course):
        self.list_courses.append(course)

    def find_student(self, student_id):
        for student in self.list_students:
            if student.identifier == student_id:
                return student
        return None


    def find_teacher(self, teacher_id):
        for teacher in self.list_teachers:
            if teacher.identifier == teacher_id:
                return teacher
        return None

    def find_course(self, course_id):
        for course in self.list_courses:
            if course.course_id == course_id:
                return course
        return None

    def register_student_to_course(self, student_id, course_id):
        student = self.find_student(student_id)
        course = self.find_course(course_id)

    def register_student_for_course(self, student_id, course_id):
        student = self.find_student(student_id)
        course = self.find_course(course_id)

        if student and course:
            course.add_student(student)
            student.add_course(course.name)
            print(f"Студента {student.name} {student.last_name} зареєстровано на курс '{course.name}'.")
        else:
            if not student:
                print(f"Помилка: Студента з ID '{student_id}' не знайдено.")
            if not course:
                print(f"Помилка: Курсу з ID '{course_id}' не знайдено.")

    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)