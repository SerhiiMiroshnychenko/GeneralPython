import pandas as pd

# Завантаження даних з файлів
ftr_task1_df = pd.read_excel('/home/smiroshnychenko/Coffee-Project/FTR/FTR-task-1.xlsx')
quants_df = pd.read_excel('/home/smiroshnychenko/Coffee-Project/FTR/Quants (stock.quant) (33).xlsx')

# Отримання унікальних значень поля Lot/Serial Number з обох файлів
ftr_lot_serial_numbers = set(ftr_task1_df['Lot/Serial Number'])
quants_lot_serial_numbers = set(quants_df['Lot/Serial Number'])

# Відбір рядків, які мають Lot/Serial Number лише в файлі FTR-task-1.xlsx
filtered_rows = ftr_task1_df[ftr_task1_df['Lot/Serial Number'].isin(ftr_lot_serial_numbers - quants_lot_serial_numbers)]

# Збереження результату в новий файл
filtered_rows.to_excel('/home/smiroshnychenko/Coffee-Project/FTR/Filtered_Result.xlsx', index=False)
