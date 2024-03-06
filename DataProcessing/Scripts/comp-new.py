import pandas as pd

# Завантаження даних з файлів
file_path_task = '/home/smiroshnychenko/Coffee-Project/Files/FHK-Task2.xlsx'
file_path_prod = '/home/smiroshnychenko/Coffee-Project/Files/FHK-Prod2.xlsx'

# Зчитування файлів у DataFrame об'єкти
df_task = pd.read_excel(file_path_task)
df_prod = pd.read_excel(file_path_prod)

# Об'єднання за допомогою значення Lot/Serial Number
merged_df = pd.merge(df_task, df_prod, on='Lot/Serial Number', how='left', suffixes=('_Task', '_Prod'))

# Визначення значення для стовбців Product та Lot/Serial Number
merged_df['Product'] = merged_df['Product_Prod'].fillna(merged_df['Product_Task'])
merged_df['Lot/Serial Number'] = merged_df['Lot/Serial Number'].fillna('NEW')

# Визначення значення для стовбця Excessive
merged_df['Excessive'] = merged_df['Product_Prod'].notnull() & merged_df['Product_Task'].isnull()

# Визначення значення для стовбця Diff
merged_df['Diff'] = (merged_df['Quantity_Task'] != merged_df['Quantity_Prod']).astype(int)

# Вибір необхідних стовбців
result_df = merged_df[['Product', 'Lot/Serial Number', 'Quantity_Task', 'Quantity_Prod', 'Excessive', 'Diff']]

# Запис результату у файл
result_file_path = '/home/smiroshnychenko/Coffee-Project/Files/ResultFHK-3.xlsx'
result_df.to_excel(result_file_path, index=False)
