from collections import Counter


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print("====== Task1 ======")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
repetitions = Counter(student['first_name'] for student in students)
for name in repetitions:
    print(f"{name}: {repetitions[name]}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

print("====== Task2 ======")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
repetitions = Counter(student['first_name'] for student in students)
most_common_name = max(repetitions, key=repetitions.get)
print(f'Самое частое имя среди учеников: {most_common_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print("====== Task3 ======")
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},# ???

        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i, students_in_class in enumerate(school_students, start=1):
    repetitions = Counter(student['first_name'] for student in students_in_class)
    most_common_name = max(repetitions, key=repetitions.get)
    print(f"Most common name in class {i}: {most_common_name}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print("====== Task4 ======")
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    males = 0
    females = 0
    for student in school_class['students']:
        if is_male.get(student['first_name']):
            males += 1
        else:
            females += 1
    print(f'Class {school_class["class"]}: females: {females}, males {males}')



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print("====== Task5 ======")
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

students_by_gender = []
for school_class in school:
    a = [x for x in school_class['students'] if is_male.get(x['first_name'])]
    b = [x for x in school_class['students'] if not is_male.get(x['first_name'])]
    students_by_gender.append({'class': school_class['class'], 'males': len(a), 'females': len(b)})
more_males = max(students_by_gender, key=lambda x: x['males'])
more_females = max(students_by_gender, key=lambda x: x['females'])
print('Больше всего мальчиков в классе ', more_males['class'])
print('Больше всего девочек в классе ', more_females['class'])







