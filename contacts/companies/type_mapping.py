import pandas as pd

# Шлях до файлу Excel
input_file_path = "COMPANIES-6.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)


# Функція для заміни значень в стовбці user_id/id
def replace_type_id(value):
    replacements = {
        "Shipping": "Delivery Address",
        "Default": "Contact",

    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['type'] = df['type'].apply(replace_type_id)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "COMPANIES-7.xlsx"
df.to_excel(output_file_path, index=False)
