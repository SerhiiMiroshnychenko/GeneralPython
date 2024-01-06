import pandas as pd

# Зчитування даних з файлів
df_full = pd.read_csv('/home/smiroshnychenko/Runex3/data/products/full.csv')
df_uniq = pd.read_csv('/home/smiroshnychenko/Runex3/data/products/uniq.csv')

# Відбір рядків, де значення поля 'default_code' збігається з uniq.csv
df_extract = df_full[df_full['default_code'].isin(df_uniq['default_code'])]

# Запис у файл extract.csv
df_extract.to_csv('/home/smiroshnychenko/Runex3/data/products/extract.csv', index=False)
