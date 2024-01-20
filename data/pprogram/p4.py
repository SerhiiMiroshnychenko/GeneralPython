import pandas as pd

# Зчитування даних з файлів
df_template_8 = pd.read_csv('product.template-8.csv')
df_product_16 = pd.read_csv('Product(product.template)-16.csv')

# Знаходження унікальних значень default_code, які є в template-8.csv, але відсутні в Product(product.template)-16.csv
unique_default_code = df_template_8[~df_template_8['default_code'].isin(df_product_16['default_code'])]

# Запис у файл uniq.csv
unique_default_code.to_csv('uniq.csv', index=False)
