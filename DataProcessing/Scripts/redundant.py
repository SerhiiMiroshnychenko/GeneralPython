import pandas as pd

# Завантажуємо дані з файлів
file_path_prod = '/home/smiroshnychenko/Coffee-Project/Files/Prod-LPS (копія).xlsx'
file_path_task = '/home/smiroshnychenko/Coffee-Project/Files/Task-LPS (копія).xlsx'

# Зчитуємо файли у DataFrame об'єкти
df_prod = pd.read_excel(file_path_prod)
df_task = pd.read_excel(file_path_task)

# Знаходимо продукти, які мають Lot/Serial Number в файлі prod, але відсутні в файлі task
missing_lot_serial = df_prod[~df_prod['Lot/Serial Number'].isin(df_task['Lot/Serial Number'])]

# Записуємо результат у файл "Зайві.xlsx"
output_file_path = '/home/smiroshnychenko/Coffee-Project/Files/Зайві.xlsx'
missing_lot_serial.to_excel(output_file_path, index=False)
