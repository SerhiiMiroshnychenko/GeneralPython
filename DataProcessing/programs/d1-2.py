import pandas as pd

# Зчитуємо дані з файлу duplicates.csv
file_path = "duplicates.csv"
df_duplicates = pd.read_csv(file_path)

# Відбираємо рядки, де значення полів "id 1" та "id 2" різні
unique_duplicates_df = df_duplicates[df_duplicates['id 1'] != df_duplicates['id 2']]

# Записуємо результат у файл uniq_dupl.csv
unique_duplicates_df.to_csv("uniq_dupl.csv", index=False)
