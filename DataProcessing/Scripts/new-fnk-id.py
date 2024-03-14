import pandas as pd

# Завантаження даних з файлів
file_path_result = '/home/smiroshnychenko/Coffee-Project/FTR/FTR-task-1.xlsx'
file_path_all_products = '/home/smiroshnychenko/Coffee-Project/New-Files/AllProducts.xlsx'
output_file_path = '/home/smiroshnychenko/Coffee-Project/New-Files/ResNewFTR.xlsx'

# Зчитування даних у DataFrame об'єкти
df_result = pd.read_excel(file_path_result)
df_all_products = pd.read_excel(file_path_all_products)

# Об'єднання за допомогою значення Lot/Serial Number
merged_df = pd.merge(df_result, df_all_products, on='Lot/Serial Number', how='left', suffixes=('_Task', '_Prod'))

# Вибір необхідних стовбців
result_df = merged_df[['Product_Task', 'Lot/Serial Number', 'Quantity', 'Product_Prod', 'Product/External ID']]

# Запис результату у файл
result_df.to_excel(output_file_path, index=False)
