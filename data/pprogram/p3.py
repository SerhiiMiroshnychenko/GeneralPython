import pandas as pd

# Зчитування даних з файлів
df_product_8 = pd.read_csv('product.template-8.csv')
df_product_16 = pd.read_csv('Product(product.template)-16.csv')

# Об'єднання даних за умовою, що значення в стовпці 'default_code' є однаковими
df_merged = pd.merge(df_product_16, df_product_8, how='outer', on='default_code', suffixes=('-16', '-8'))

# Вибірка потрібних полів для product_8-16.csv
result_df = df_merged[["default_code", "name-8", "name-16", "id-8", "id-16"]]

# Запис у файл product_8-16.csv
result_df.to_csv('product_16-8.csv', index=False)
