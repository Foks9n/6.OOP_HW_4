class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self, count):
        """ Подсчитывает среднее значение заданного объекта, универсальный метод """
        return round(sum(sum(count.values(), [])) / len(sum(count.values(), [])), 1)


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average(self.grades)}'
                f' \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, Student):
        return self.average < Student.average

    def __gt__(self, Student):
        return self.average > Student.average

    def __eq__(self, Student):
        return self.average == Student.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average(self, count):
        """ Подсчитывает среднее значение заданного объекта, универсальный метод """
        return round(sum(sum(count.values(), [])) / len(sum(count.values(), [])), 1)


    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average(self.grades)}')


    def __lt__(self, Lecturer):
        return self.average < Lecturer.average

    def __gt__(self, Lecturer):
        return self.average > Lecturer.average

    def __eq__(self, Lecturer):
        return self.average == Lecturer.average


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
        return (f'Имя: {self.name} \nФамилия: {self.surname}')


student_1 = Student('Klement', 'Ivanov', 'm')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Aleksandr', 'Kostylev', 'm')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Sergey', 'Kuzmin')
reviewer_1.courses_attached += ['Python', 'Git']

lecturer_1 = Lecturer('Alexey', 'Bulkin')
lecturer_1.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)

reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 6)
reviewer_1.rate_hw(student_2, 'Git', 8)

student_1.rate_lec(lecturer_1 , 'Python', 10)
student_1.rate_lec(lecturer_1 , 'Python', 9)
student_1.rate_lec(lecturer_1 , 'Python', 9)

student_2.rate_lec(lecturer_1 , 'Python', 10)
student_2.rate_lec(lecturer_1 , 'Python', 10)
student_2.rate_lec(lecturer_1 , 'Python', 7)

student_1.rate_lec(lecturer_1 , 'Git', 7)
student_1.rate_lec(lecturer_1 , 'Git', 6)
student_1.rate_lec(lecturer_1 , 'Git', 9)

student_2.rate_lec(lecturer_1 , 'Git', 9)
student_2.rate_lec(lecturer_1 , 'Git', 8)
student_2.rate_lec(lecturer_1 , 'Git', 7)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1]

#средняя оценка всех студентов за ДЗ по курсу
def average_grade_course_student(students_list, course):
    avg_grade = []
    for student in students_list:
        if course in student.grades:
            avg_grade += student.grades[course]
    if avg_grade:
        return round(sum(avg_grade) / len(avg_grade), 1)

#средняя оценка лекторов за ДЗ по курсу
def average_grade_course_lecturer(lecturers_list, course):
    avg_grade = []
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            avg_grade += lecturer.grades[course]
    if avg_grade:
        return round(sum(avg_grade) / len(avg_grade), 1)


print (f'Студенты: \n{student_1} \n{student_2}')
print ()
print (f'Лекторы: \n{lecturer_1}')
print ()
print (f'Проверяющие: \n{reviewer_1}')
print ()
print(average_grade_course_lecturer(lecturers_list, 'Python'))
print(average_grade_course_student(students_list, 'Python'))
print(average_grade_course_lecturer(lecturers_list, 'Git'))
print(average_grade_course_student(students_list, 'Git'))