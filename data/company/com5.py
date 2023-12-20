import pandas as pd

# Шляхи до файлів
file_path1 = "/home/smiroshnychenko/Runex3/data/company/res.partner (12).csv"
file_path2 = "/home/smiroshnychenko/Runex3/data/company/com_map.csv"

# Зчитуємо DataFrame з файлів
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Об'єднуємо два DataFrame за полем "old_id"
merged_df = pd.merge(df1, df2, how='left', left_on='parent_id/id', right_on='old_id')

# Замінюємо значення поля "parent_id/id" на значення поля "new_id" там, де вони співпадають
df1['parent_id/id'] = merged_df['new_id'].fillna(df1['parent_id/id'])

# Записуємо результат у файл "res.partner (12)_updated.csv"
df1.to_csv("/home/smiroshnychenko/Runex3/data/company/res.partner (12)_updated.csv", index=False)

print("Updated file 'res.partner (12)_updated.csv' has been created.")
