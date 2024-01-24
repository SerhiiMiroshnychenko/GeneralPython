import pandas as pd

# Завантаження даних
supplier_info = pd.read_csv('supplier_info.csv')
contact_info = pd.read_csv('Contact (res.partner) (2).csv')

# Злиття даних за допомогою merge
merged_data = pd.merge(contact_info, supplier_info, left_on='ID', right_on='partner_id', how='left')

# Відбір необхідних полів
result_data = merged_data[['External ID', 'ID', 'Name', 'id']].rename(columns={'id': 'Supplier ID'})

# Збереження результату в файл
result_data.to_csv('sum_data.csv', index=False)

print("Операція завершена. Результат збережено в sum_data.csv")
