import pandas as pd

# Шляхи до файлів
uniq_file_path = "uniq.csv"
bom_file_path = "product.template (3).csv"

# Зчитуємо DataFrame з файлів
uniq_df = pd.read_csv(uniq_file_path)
bom_df = pd.read_csv(bom_file_path)

# Обираємо рядки, де значення поля "default_code" співпадає з файлом uniq.csv
result_df = bom_df[bom_df['default_code'].isin(uniq_df['default_code'])]

# Записуємо результат у файл "result_bom.csv"
result_df.to_csv("result_bom.csv", index=False)

print("Results have been written to 'result_bom.csv'.")
