import pandas as pd

# Завантажуємо дані з файлів
file_path_task = '/home/smiroshnychenko/Coffee-Project/Files/ResultFHK-3 (копія).xlsx'
file_path_prod = '/home/smiroshnychenko/Coffee-Project/Files/FHK-prod (копія).xlsx'

# Зчитуємо файли у DataFrame об'єкти
df_task = pd.read_excel(file_path_task)
df_prod = pd.read_excel(file_path_prod)

# Злиття даних за допомогою значення Lot/Serial Number
result_df = pd.merge(df_prod, df_task, on='Lot/Serial Number', how='left', suffixes=('_Prod', '_Task'))

# Встановлення значень Excessive та Diff
result_df['Excessive'] = result_df.apply(lambda row: 1 if pd.isna(row['Product_Task']) else 0, axis=1)
result_df['Diff'] = result_df.apply(lambda row: 1 if row['Quantity_Prod'] != row['Quantity_Task'] else 0, axis=1)

# Вибір необхідних стовбців
result_df = result_df[['Product_Prod', 'Lot/Serial Number', 'Quantity_Task', 'Quantity_Prod',
                       'Excessive', 'Diff', 'Location', 'Product/External ID']]

# Запис результату у файл
result_file_path = '/home/smiroshnychenko/Coffee-Project/Files/Res/ResultFHK-full2.xlsx'
result_df.to_excel(result_file_path, index=False)
