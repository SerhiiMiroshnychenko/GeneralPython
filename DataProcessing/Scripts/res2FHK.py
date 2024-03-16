import pandas as pd

# Завантаження даних з файлів
all_data = pd.read_excel("/home/smiroshnychenko/Coffee-Project/New-Files/AllFHK-2.xlsx")
task_data = pd.read_excel("/home/smiroshnychenko/Coffee-Project/New-Files/FHK-Task2.xlsx")

# Об'єднання даних за допомогою поля "Lot/Serial Number"
merged_data = pd.merge(all_data, task_data, on="Lot/Serial Number", suffixes=('_Prod', '_Task'), how='left')

# Розрахунок поля "Quantity"
merged_data['Quantity'] = merged_data['Quantity_Task'] - merged_data['Quantity_Prod']

# Вибірка потрібних стовбців (без стовбця 'Product')
result_data = merged_data[['Location', 'Lot/Serial Number', 'Product/External ID', 'Quantity_Prod', 'Quantity_Task', 'Quantity']]

# Запис даних у новий файл
result_data.to_excel("/home/smiroshnychenko/Coffee-Project/New-Files/Pesult2FHK.xlsx", index=False)






