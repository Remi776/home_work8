from input_data import data_student, data_parents
from output_data import output

job = input('Что ты хочешь сделать?\n1- Ввести данные\n2- Вывести данные\n')
if '1' in job:
    about = input('В какую таблицу ты хочешь занести данные?\n1- Ребенок\n2- Родитель\n')
    if '1' in about:
        data_student()
    else:
        data_parents()
else:
    output()