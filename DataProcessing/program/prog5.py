import pandas as pd

# Зчитуємо файли
prod_import_df = pd.read_csv('PROD-IMPORT.csv')
sum_data_df = pd.read_csv('sum_data.csv')

# Об'єднуємо дані за умовою External ID та Product Supplier/ID
merged_df = pd.merge(prod_import_df, sum_data_df, left_on='Product Supplier/ID', right_on='External ID', how='left')

# Додаємо новий стовпець Product Supplier/Database ID зі значенням Supplier ID
prod_import_df['Product Supplier/Database ID'] = merged_df['Supplier ID']

# Записуємо результат в файл RESULT.csv
prod_import_df.to_csv('RESULT.csv', index=False)

