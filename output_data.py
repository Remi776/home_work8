def output():
    with open('students.txt', 'r', encoding='utf-8') as file:
        for i in file:
            stroka = i.split(';')
            id = stroka[0]
            name = stroka[1].split()[0]
            surname = stroka[1].split()[1]
            mark = stroka[-2]
            data = stroka[-1]
            print(f'Запись {id}:\nИмя: {name}\nФамилия; {surname}\nСредний балл: {mark}\nДата рождения: {data}')

    with open('parents.txt.txt', 'r', encoding='utf-8') as file:
        for i in file:
            stroka = i.split(';')
            id = stroka[0]
            name = stroka[1].split()[0]
            surname = stroka[1].split()[1]
            tel = stroka[-1]
            print(f'Запись {id}(Родитель):\nИмя: {name}\nФамилия; {surname}\nТелефон: {tel}\n')