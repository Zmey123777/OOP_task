class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        average_grade = sum(sum(vals) for vals in self.grades.values()) / sum(len(vals) for vals in self.grades.values()) if self.grades else 0
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}\n"

    def rate_lecture(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.rate(course, mark)
        else:
            print("Error: У данного лектора нет курсов.")
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        average_grade = self.average_grade(grades = self.lecturer_grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}\n"
    
    def rate(self, course, mark):
        if course in self.lecturer_grades:
            self.lecturer_grades[course] += [mark]
        else:
            self.lecturer_grades[course] = [mark]

    def average_grade(self, grades):
        return sum(sum(vals) for vals in grades.values()) / sum(len(vals) for vals in grades.values()) if grades else 0

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Michael', 'Schumacher', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['PHP']
bad_student = Student('Ilya', 'Oblomov', 'male')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['PHP']
bad_student.finished_courses += ['PHP']
 
cool_mentor = Reviewer('Boris', 'Elcin')
cool_mentor.courses_attached += ['Python']
bad_mentor = Reviewer('Iosif', 'Stalin')
bad_mentor.courses_attached += ['PHP']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
bad_mentor.rate_hw(bad_student, 'PHP', 2)

lecturer = Lecturer('Vasiliy', 'Chapaev')
lecturer.courses_attached += ['Python']
best_student.rate_lecture(lecturer, 'Python', 5)
best_student.rate_lecture(lecturer, 'Python', 7)
best_student.rate_lecture(lecturer, 'Python', 9)
cool_lecturer = Lecturer('Stenka', 'Razin')
cool_lecturer.courses_attached += ['PHP']
bad_student.rate_lecture(cool_lecturer, 'PHP', 10)

print(best_student)
print(bad_student)
print(lecturer)
print(cool_lecturer)
print(cool_mentor)
