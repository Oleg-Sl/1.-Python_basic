import random


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, lastname, name, secondname):
        self.lastname = lastname
        self.name = name
        self.secondname = secondname

    def __str__(self):
        return f'{self.lastname} {self.name[0]}. {self.secondname[0]}.'


class Parent(Person):
    def __init__(self, *args):
        super().__init__(*args)


class Teacher(Person):
    def __init__(self, lastname, name, secondname, subject):
        super().__init__(lastname, name, secondname)
        self.subject = subject


class ClassRoom:
    def __init__(self, number, char, teachers):
        self.number = number
        self.char = char
        self.teachers = teachers

    def __str__(self):
        return f'{self.number}{self.char}'

    def __repr__(self):
        return f'{self.number}{self.char}'

    def get_teachers(self):
        return [str(teacher) for teacher in self.teachers]

    def get_room(self):
        return f'{self.number}{self.char}'


class Student(Person):
    def __init__(self, lastname, name, secondname, parent_men, parent_women, class_room):
        self.parent_men = parent_men
        self.parent_women = parent_women
        self.class_room = class_room
        super().__init__(lastname, name, secondname)

    def get_parents(self):
        return f'{self.parent_men.lastname} {self.parent_men.name[0]}.{self.parent_men.secondname[0]}., ' \
               f'{self.parent_women.lastname} {self.parent_women.name[0]}.{self.parent_women.secondname[0]}.'

    def get_subjects(self):
        return [teacher.subject for teacher in self.class_room.teachers]


class School:
    def __init__(self,):
        self.teachers = []
        self.class_rooms = []
        self.students = []

    def add_teacher(self, *args):
        self.teachers.append(Teacher(*args))

    def add_class_room(self, number, char, teacher):
        self.class_rooms.append(ClassRoom(number, char, teacher))

    def add_student(self, lastname, name, secondname, parent_men, parent_women, class_room):
        self.students.append(Student(lastname, name, secondname, Parent(*parent_men), Parent(*parent_women), class_room))

    def get_class_rooms(self):
        return [room for room in self.class_rooms]
        # return [f'{room.number} {room.char}' for room in self.class_rooms]

    def get_student_by_room(self, str_room):
        return [str(student) for student in self.students if student.class_room.get_room() == str_room]

    def get_subjects(self, student):
        ind = self.students.index(student)
        return self.students[ind].get_subjects()

    def get_parents(self, student):
        ind = self.students.index(student)
        return self.students[ind].get_parents()

    def get_teacher_in_room(self, room):
        ind = self.class_rooms.index(room)
        return self.class_rooms[ind].get_teachers()


teachers = [
    ['Иванов1', 'Илья1', 'Иванович1', 'Математика'],
    ['Иванов2', 'Илья2', 'Иванович2', 'Биология'],
    ['Иванов3', 'Илья3', 'Иванович3', 'Физика'],
    ['Иванов4', 'Илья4', 'Иванович4', 'Информатика'],
    ['Иванов5', 'Илья5', 'Иванович5', 'История'],
]

school = School()

# добавление списка учителей в школу
school.add_teacher('Иванов_1', 'Илья_1', 'Иванович_1', 'Математика')
school.add_teacher('Иванов_2', 'Илья_2', 'Иванович_2', 'Биология')
school.add_teacher('Иванов_3', 'Илья_3', 'Иванович_3', 'Физика')
school.add_teacher('Иванов_4', 'Илья_4', 'Иванович_4', 'Информатика')
school.add_teacher('Иванов_5', 'Илья_5', 'Иванович_5', 'История')
# print(school.teachers)

# добавление классов школы
for number in range(4, 7):
    for char in 'АБ':
        school.add_class_room(number, char, random.sample(school.teachers, 3))
# print(school.class_rooms)

# добавление учеников в класс школы
school.add_student(
    'Иванов',
    'Илья',
    'Иванович',
    ['Иванов', 'Иван', 'Иванович'],
    ['Иванова', 'Ирина', 'Ивановна'],
    school.class_rooms[0]
)
school.add_student(
    'Николаев',
    'Константин',
    'Николаевич',
    ['Николаев', 'Николай', 'Николаевич'],
    ['Николаева', 'Наталья', 'Николаевна'],
    school.class_rooms[1]
)
school.add_student(
    'Петрова',
    'Анастасия',
    'Пертровна',
    ['Петров', 'Петр', 'Петрович'],
    ['Петрова', 'Адексанлпа', 'Петровна'],
    school.class_rooms[1]
)
school.add_student(
    'Сидоров',
    'Андрей',
    'Иванович',
    ['Сидоров', 'Иван', 'Иванович'],
    ['Сидорова', 'Ирина', 'Ивановна'],
    school.class_rooms[5]
)
school.add_student(
    'Овечкина',
    'Софья',
    'Николаевна',
    ['Овечкин', 'Николай', 'Николаевич'],
    ['Овечкина', 'Наталья', 'Николаевна'],
    school.class_rooms[5]
)
# print(school.students)


print('Список всех классов школы: ', school.get_class_rooms())

print(f'Список всех учеников в "4Б" классе: ', school.get_student_by_room('4А'))
print(f'Список всех учеников в "4Б" классе: ', school.get_student_by_room('4Б'))
print(f'Список всех учеников в "4Б" классе: ', school.get_student_by_room('5Б'))

print(f'Список всех предметов ученика "{school.students[0]}": ', school.get_subjects(school.students[0]))
print(f'Список всех предметов ученика "{school.students[2]}": ', school.get_subjects(school.students[2]))
print(f'Список всех предметов ученика "{school.students[4]}": ', school.get_subjects(school.students[4]))

print(f'ФИО родителей ученика "{school.students[1]}": ', school.get_parents(school.students[1]))
print(f'ФИО родителей ученика "{school.students[2]}": ', school.get_parents(school.students[2]))
print(f'ФИО родителей ученика "{school.students[3]}": ', school.get_parents(school.students[3]))

print(f'Список всех Учителей, преподающих в "{school.class_rooms[0]}" классе', school.get_teacher_in_room(school.class_rooms[0]))
print(f'Список всех Учителей, преподающих в "{school.class_rooms[2]}" классе', school.get_teacher_in_room(school.class_rooms[2]))
print(f'Список всех Учителей, преподающих в "{school.class_rooms[3]}" классе', school.get_teacher_in_room(school.class_rooms[3]))



