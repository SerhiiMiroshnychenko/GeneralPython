import csv
from collections import defaultdict


def find_duplicates(input_file, output_file):
    # Відкриття файлу для читання
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        # Створення словника для зберігання інформації про дублікати
        duplicates = defaultdict(list)

        # Перегляд кожного рядка вхідного файлу
        for row in reader:
            name = row['name']
            email = row['email']
            record_id = row['id']

            # Додавання рядка до словника дублікатів
            duplicates[(name, email)].append((record_id, row))

    # Відкриття файлу для запису дублікатів
    with open(output_file, 'w', newline='') as duplicate_file:
        fieldnames = ['name', 'email', 'id 1', 'id 2']
        writer = csv.DictWriter(duplicate_file, fieldnames=fieldnames)
        writer.writeheader()

        # Запис дублікатів у файл
        for key, records in duplicates.items():
            if len(records) > 1:
                for i, (record_id, row) in enumerate(records):
                    if i > 0:
                        writer.writerow({
                            'name': row['name'],
                            'email': row['email'],
                            'id 1': records[0][0],
                            'id 2': record_id
                        })


# Виклик функції з вказанням шляху до вхідного та вихідного файлів
find_duplicates('/home/smiroshnychenko/Runex3/data/duplicates/data_files/Contact (res.partner) (9).csv',
                '/home/smiroshnychenko/Runex3/data/duplicates/data_files/duplicates3.csv')
