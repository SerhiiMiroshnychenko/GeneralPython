import pandas as pd

# Шлях до вхідного файлу
input_file_path = "/home/smiroshnychenko/Runex3/data/company/res.partner (12).csv"

# Зчитуємо дані з файлу
df = pd.read_csv(input_file_path)

# Копіюємо DataFrame для зручності
new_df = df.copy()

# Замінюємо значення в полі "parent_id/id"
new_df["parent_id/id"] = new_df["parent_id/id"].astype(str).apply(lambda x: f"__import__.res_partner_legacy_{x.split('_')[-1]}")

# Записуємо результат у файл "new_company.csv"
output_file_path = "/home/smiroshnychenko/Runex3/data/company/new_company.csv"
new_df.to_csv(output_file_path, index=False)

print(f"File '{output_file_path}' has been created.")

