class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        all_grades = []
        for course, grade in self.grades.items():
            all_grades.extend(grade)
        avg_grades = sum(all_grades)/len(all_grades)
        return avg_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_rate()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'                                 \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avg_rate() < other.avg_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_grades = {}

    def avg_rate(self):
        all_grades = []
        for course, grades in self.courses_grades.items():
            all_grades.extend(grades)
        avg_grades = sum(all_grades)/len(all_grades)
        return avg_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avg_rate() < other.avg_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.courses_in_progress += ['HTML']
best_student.finished_courses += ['Введение в программирование']

worst_student = Student('Eman', 'Ruoy', 'your_gender')
worst_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

bad_reviewer = Reviewer('Buddy', 'Some')
bad_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Haris', 'Mitchel')
cool_lecturer.courses_attached += ['HTML']
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Mitchel', 'Haris')
bad_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(worst_student, 'Python', 1)
cool_reviewer.rate_hw(worst_student, 'Python', 1)

best_student.rate_lector(cool_lecturer, 'HTML', 10)
best_student.rate_lector(cool_lecturer, 'HTML', 11)
best_student.rate_lector(cool_lecturer, 'HTML', 5)
best_student.rate_lector(cool_lecturer, 'Python', 3)
best_student.rate_lector(bad_lecturer, 'Python', 10)

print(cool_lecturer.courses_grades)
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(best_student < worst_student)
print()
print(cool_lecturer < bad_lecturer)


def avg_rate_for_students(students, course):
    rates = []
    for student in students:

        for courses, grades in student.grades.items():
            if courses == course:
                rates.extend(grades)
    avg_rates = sum(rates) / len(rates)

    return avg_rates


student_list = [best_student, worst_student]
print(avg_rate_for_students(student_list, 'Python'))


def avg_rate_for_lecturers(lecturers, course):
    rates = []
    for lecturer in lecturers:
        for courses, grades in lecturer.courses_grades.items():
            if courses == course:
                rates.extend(grades)
    avg_rates = sum(rates) / len(rates)

    return avg_rates


lecturer_list = [cool_lecturer, bad_lecturer]
print(avg_rate_for_lecturers(lecturer_list, 'Python'))
