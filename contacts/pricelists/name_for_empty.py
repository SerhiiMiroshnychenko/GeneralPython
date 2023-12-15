import csv

# Шлях до CSV-файлу
csv_path = '/home/smiroshnychenko/GeneralPython/contacts/pricelists/all_pl.csv'

# Відкриваємо CSV-файл
with open(csv_path, 'r') as csv_file:
    # Створюємо об'єкт для читання CSV
    csv_reader = csv.DictReader(csv_file)

    # Проходимо через кожен рядок у файлі
    for row in csv_reader:
        # Перевіряємо, чи відсутнє значення в полі "partner_product_pricelist/id"
        if not row.get('partner_product_pricelist/id'):
            # Виводимо значення поля "id" для відповідного рядка
            print(row['id'])
