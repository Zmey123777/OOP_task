def average_grades(grades):
        return sum(sum(vals) for vals in grades.values()) / sum(len(vals) for vals in grades.values()) if grades else 0

def compare_students(student_one, student_two):
    if not isinstance(student_one, Student) or not isinstance(student_two, Student):
        return "Ошибка: Оба объекта должны быть экземплярами класса Student."
    avg_grade_one = average_grades(student_one.grades)
    avg_grade_two = average_grades(student_two.grades)
    if avg_grade_one < avg_grade_two:
        return f"{student_one.name} {student_one.surname} имеет более низкую среднюю оценку чем {student_two.name} {student_two.surname}."
    elif avg_grade_one > avg_grade_two:
        return f"{student_one.name} {student_one.surname} имеет более высокую среднюю оценку чем {student_two.name} {student_two.surname}."
    else:
        return f"Средняя оценка {student_one.name} {student_one.surname} и {student_two.name} {student_two.surname} одинакова."

def compare_lecturers(lecturer_one, lecturer_two):
    if not isinstance(lecturer_one, Lecturer) or not isinstance(lecturer_two, Lecturer):
        return "Ошибка: Оба объекта должны быть экземплярами класса Lecturer."
    avg_grade_one = average_grades(lecturer_one.lecturer_grades)
    avg_grade_two = average_grades(lecturer_two.lecturer_grades)
    if avg_grade_one < avg_grade_two:
        return f"{lecturer_one.name} {lecturer_one.surname} имеет более низкую среднюю оценку за лекции чем {lecturer_two.name} {lecturer_two.surname}."
    elif avg_grade_one > avg_grade_two:
        return f"{lecturer_one.name} {lecturer_one.surname} имеет более высокую среднюю оценку за лекции чем {lecturer_two.name} {lecturer_two.surname}."
    else:
        return f"Средняя оценка за лекции {lecturer_one.name} {lecturer_one.surname} и {lecturer_two.name} {lecturer_two.surname} одинакова."
    
def average_students_grades(students, course_name):
    total_sum = 0
    total_count = 0
    for student in students:
        if isinstance(student, Student) and course_name in student.grades:
            total_sum += sum(student.grades[course_name])
            total_count += len(student.grades[course_name])
    if total_count > 0:
        return total_sum / total_count
    else:
        return 0
    
def average_lecture_grades(lecturers, course_name):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.lecturer_grades:
            total_sum += sum(lecturer.lecturer_grades[course_name])
            total_count += len(lecturer.lecturer_grades[course_name])
    if total_count > 0:
        return total_sum / total_count
    else:
        return 0
    
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        average_grade = average_grades(self.grades)
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}\n"

    def rate_lecture(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.rate(course, mark)
        else:
            print("Ошибка: У данного лектора нет курсов.")
        
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
        average_grade = average_grades(grades = self.lecturer_grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}\n"
    
    def rate(self, course, mark):
        if course in self.lecturer_grades:
            if 1 <= mark <= 10:
                self.lecturer_grades[course] += [mark]
            else:
                print(f"Ошибка: Оценка ({mark}) должна быть от 1 до 10.")
        else:
            self.lecturer_grades[course] = [mark]

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
print(compare_students(best_student, bad_student))
print(compare_lecturers(lecturer, cool_lecturer))
print(average_students_grades([best_student, bad_student], 'Python'))
print(average_lecture_grades([lecturer, cool_lecturer], 'Python'))
