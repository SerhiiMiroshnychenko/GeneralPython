import pandas as pd

# Зчитування даних з файлів
df_full = pd.read_csv('full.csv')
df_uniq = pd.read_csv('uniq.csv')

# Відбір рядків, де значення поля 'default_code' збігається з uniq.csv
df_extract = df_full[df_full['default_code'].isin(df_uniq['default_code'])]

# Запис у файл extract.csv
df_extract.to_csv('extract.csv', index=False)
