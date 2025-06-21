class Gradebook:
    def __init__(self):
        self.list_grades = []

    def add_grade(self, grade):
        self.list_grades.append(grade)

    def get_student_grades(self, student):
        result = []
        for grade in self.list_grades:
            if grade.student == student:
                result.append(grade.grade)
        return result

    def get_student_average(self, student):
        grades = self.get_student_grades(student)
        if len(grades) == 0:
            return 0.0
        return sum(grades) / len(grades)

    def get_course_average(self, course):
        course_grades = []
        for grade in self.list_grades:
            if grade.course == course:
                course_grades.append(grade.grade)
        if len(course_grades) == 0:
            return 0.0
        return sum(course_grades) / len(course_grades)

    def get_students_with_average_above(self, threshold):
        result = []
        seen = set()
        for grade in self.list_grades:
            student = grade.student
            if student.identifier not in seen:
                avg = self.get_student_average(student)
                if avg > threshold:
                    result.append(f"{student.name} {student.last_name} (Середній бал: {avg})")
                seen.add(student.identifier)
        return result

    def get_courses_with_average_above(self, threshold):
        result = []
        seen = set()
        for grade in self.list_grades:
            course = grade.course
            if course.course_id not in seen:
                avg = self.get_course_average(course)
                if avg > threshold:
                    result.append(f"{course.name} (Середній бал: {avg})")
                seen.add(course.course_id)
        return result
