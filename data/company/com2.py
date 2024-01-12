import pandas as pd

# Шлях до файлу
file_path = "new_company.csv"

# Зчитуємо DataFrame з файлу
df = pd.read_csv(file_path)

# Видаляємо рядки, де значення в колонці "parent_id/id" дорівнює "__import__.res_partner_legacy_nan"
df = df[df["parent_id/id"] != "__import__.res_partner_legacy_nan"]

# Записуємо оновлений DataFrame назад у файл
df.to_csv(file_path, index=False)

print(f"Rows with 'parent_id/id' equal to '__import__.res_partner_legacy_nan' have been removed.")
