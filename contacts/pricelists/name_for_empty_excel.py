import openpyxl

# Шлях до Excel-файлу
excel_path = '/home/smiroshnychenko/GeneralPython/contacts/pricelists/all_sales_pricelists.xlsx'

# Відкриваємо Excel-файл
workbook = openpyxl.load_workbook(excel_path)
# Вибираємо активний лист
sheet = workbook.active

# Проходимо через кожен рядок у файлі
for row in sheet.iter_rows(min_row=2, values_only=True):
    # Перевіряємо, чи відсутнє значення в полі "partner_product_pricelist/id"
    if row[1] is None:
        # Виводимо значення поля "id" для відповідного рядка
        print(row[0])
    if row[0] is None:
        # Виводимо значення поля "id" для відповідного рядка
        print('Empty name')

# Закриваємо файл
workbook.close()
