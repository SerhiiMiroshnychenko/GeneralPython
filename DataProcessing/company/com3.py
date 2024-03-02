import pandas as pd

# Шлях до файлу
file_path = "Contact (res.partner) (14).csv"

# Зчитуємо DataFrame з файлу
df = pd.read_csv(file_path)

# Видаляємо рядки, де значення в колонці "is_company" не дорівнює "True"
df = df[df["is_company"] == True]

# Записуємо оновлений DataFrame назад у файл
df.to_csv(file_path, index=False)

print("Rows with 'is_company' not equal to 'True' have been removed.")
