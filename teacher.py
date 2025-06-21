from person import Person

class Teacher(Person):
    def __init__(self, name, last_name, identifier, courses):
        super().__init__(name, last_name,identifier)
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)

    def list_course(self):
        return f"Список курсів: {','.join(self.courses)}"