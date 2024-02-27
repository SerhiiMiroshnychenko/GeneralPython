import pandas as pd

# Завантаження даних з файлів
all_products_df = pd.read_excel('/home/smiroshnychenko/Coffee-Project/New-Files/AllProducts.xlsx')
task2_df = pd.read_excel('/home/smiroshnychenko/Coffee-Project/FTR/FTR-task-1.xlsx')

# Створення словника для швидшого доступу до значень Product/External ID за Lot/Serial Number
external_id_dict = dict(zip(all_products_df['Lot/Serial Number'], all_products_df['Product/External ID']))

# Додавання поля Product/External ID до task2_df
task2_df['Product/External ID'] = task2_df['Lot/Serial Number'].map(external_id_dict)

# Збереження результату в файл
task2_df.to_excel('/home/smiroshnychenko/Coffee-Project/FTR/FTR-task-1.xlsx', index=False)
