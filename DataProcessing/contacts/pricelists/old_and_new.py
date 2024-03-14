import pandas as pd

# Шляхи до файлів
file1_path = 'res.partner (24).csv'
file2_path = 'Contact (res.partner) (15).csv'

# Зчитуємо файли у DataFrame
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Об'єднуємо файли за полем "id"
merged_df = pd.merge(df1, df2, on='id', how='left', suffixes=('_file1', '_file2'))

# Визначаємо рядки, що мають співпадіння за полем "id"
matching_rows = merged_df.dropna(subset=['name_file2'])

# Визначаємо рядки, що не мають співпадіння за полем "id"
non_matching_rows = merged_df[merged_df['name_file2'].isna()]

# Записуємо результат у файли
matching_rows[['id', 'partner_product_pricelist/id', 'name_file1']].to_csv('old_id.csv', index=False)
non_matching_rows[['id', 'partner_product_pricelist/id', 'name_file1']].to_csv('new_id.csv', index=False)
