class Person:
    def _init_(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


class Student(Person):
    def _init_(self, name, student_id):
        super()._init_(name)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


class SportsPlayer(Person):
    def _init_(self, name, sport_name):
        super()._init_(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        print("Sport Name:", self.sport_name)


class CollegeStudent(Student, SportsPlayer):
    def _init_(self, name, student_id, sport_name, college_name):
        Student._init_(self, name, student_id)
        SportsPlayer._init_(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        self.display_person()
        self.display_student()
        self.display_sports_player()
        print("College Name:", self.college_name)


student1 = CollegeStudent(
    "Pratham",
    "CS101",
    "Cricket",
    "ABC Engineering College"
)

student1.display_college_student()