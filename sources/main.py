import csv
import os
import random
from collections import OrderedDict

teachers = []
with open('csv_files/Teachers.csv', encoding='utf-8') as file:
    content = csv.DictReader(file)

    for row in content:
        teachers.append(row)

students = []
for filename in os.listdir('csv_files'):
    if filename == 'Teachers.csv' or not filename.endswith('.csv'):
        continue
    with open(f'csv_files/{filename}', encoding='utf-8') as file:
        content = csv.DictReader(file)

        for row in content:
            students.append(row)

results = []
for teacher in teachers:
    data = teacher['Количество']
    if 'зачет' in data:
        num = int(data.split()[0])
        value = 'Зачет'
    else:
        num, value = [int(string) for string in data.split() if string.isdigit()]
        value = str(value) + ' баллов'

    name, group = random.choice([[s['ФИО'], s['Номер в списке']] for s in students if s['Группа'] == teacher['Группа'] and s['ФИО'] not in [res['Имя студента'] for res in results if res['Предмет'] == teacher['Предмет']]])

    d = {
        'Преподаватель': teacher['Преподаватель'],
        'Предмет': teacher['Предмет'],
        'Группа': teacher['Группа'],
        'Имя студента': name,
        'Номер в списке': group,
        'Количество баллов': value,
    }

    results.append(OrderedDict(d))

with open('result.txt', 'w', encoding='utf-8') as file:
    for line in results:
        for element in line:
            file.write('{}, '.format(line[element]))
        file.write('\n')
