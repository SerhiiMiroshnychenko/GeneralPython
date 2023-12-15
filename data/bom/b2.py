import pandas as pd

# Шлях до файлу result_bom.csv
result_bom_file_path = "/home/smiroshnychenko/Runex3/data/bom/result_bom.csv"

# Зчитуємо DataFrame з файлу result_bom.csv
result_bom_df = pd.read_csv(result_bom_file_path)

# Вибираємо рядки, де поле "bom_ids/id" не є порожнім
bom_df = result_bom_df[result_bom_df['bom_ids/id'].notna()]

# Записуємо результат у файл "bom.csv"
bom_df.to_csv("/home/smiroshnychenko/Runex3/data/bom/bom.csv", index=False)

print("Results have been written to 'bom.csv'.")
