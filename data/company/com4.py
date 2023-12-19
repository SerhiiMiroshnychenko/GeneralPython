import pandas as pd

# Шляхи до файлів
file_path1 = "/home/smiroshnychenko/Runex3/data/company/Contact (res.partner) (14).csv"
file_path2 = "/home/smiroshnychenko/Runex3/data/company/res.partner (13).csv"

# Зчитуємо DataFrame з файлів
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Об'єднуємо два DataFrame за полем "name"
merged_df = pd.merge(df1, df2, how='inner', on='name')

# Створюємо новий DataFrame для запису результатів
result_df = pd.DataFrame({
    'name': merged_df['name'],
    'old_id': merged_df['id_y'],
    'new_id': merged_df['id_x']
})

# Записуємо результат у файл "com_map.csv"
result_df.to_csv("/home/smiroshnychenko/Runex3/data/company/com_map.csv", index=False)

print("Mapping file 'com_map.csv' has been created.")
