def data_student():
    name = input('Введите свое имя: ')
    surname = input('Введите свою фамилию: ')
    mark = input('Введите средний балл: ')
    date_of_birth = input('Введите дату рождения: ')

    with open('students.txt', 'r', encoding='utf-8') as file:
        id = file.readlines()[-1].split(';')[0]

    with open('students.txt', 'a', encoding='utf-8') as file:
        file.write(f'{int(id) + 1};{name} {surname};{mark};{date_of_birth}\n')


def data_parents():
    name = input('Введите свое имя: ')
    surname = input('Введите свою фамилию: ')
    tel = input('Введите свой рабочий телефон: ')
    flag = False
    with open('students.txt', 'r', encoding='utf-8') as file:
       FIO = file.readlines()

    for row in FIO:
        if surname in row:
            flag = True
            id = row.split(';')[0]
            break
    else:
        print(f'Не найден ребенок с такой фамилией {surname}')
    if flag:
        with open('parents.txt', 'a', encoding='utf-8') as file:
            file.write(f'{id};{name} {surname};{tel}\n')