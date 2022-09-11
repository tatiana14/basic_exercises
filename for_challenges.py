# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

print("====== Task1 ======")
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

print("====== Task2 ======")
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f'{name}: {len(name)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

print("====== Task3 ======")
is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in is_male:
    gender = 'male' if is_male[name] else 'female'
    print(name, gender)


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

print("====== Task4 ======")
groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
print(f'Total groups count {len(groups)}')
for i, group in enumerate(groups, start=1):
    print(f'Group {i}: {len(group)} students')

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

print("====== Task5 ======")
groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
for i, group in enumerate(groups, start=1):
    print(f"Group {i}: {', '.join(group)}")
