import pandas as pd

# Шлях до файлу CSV
csv_file_path = '/home/smiroshnychenko/GeneralPython/contacts/pricelists/Contact (res.partner) (15).csv'

# Зчитуємо CSV у DataFrame
df = pd.read_csv(csv_file_path)

# Записуємо DataFrame у XLSX
xlsx_file_path = '/home/smiroshnychenko/GeneralPython/contacts/pricelists/Contact(res.partner).xlsx'
df.to_excel(xlsx_file_path, index=False, engine='openpyxl')

print(f"Файл {xlsx_file_path} успішно створено.")
