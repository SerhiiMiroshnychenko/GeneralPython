import pandas as pd

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-4.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)


# Функція для заміни значень в стовбці user_id/id
def replace_pl_id(value):
    replacements = {
        "purchase.list0": "__export__.product_pricelist_08",
    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['property_product_pricelist_purchase/id'] = df['property_product_pricelist_purchase/id'].apply(replace_pl_id)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-5.xlsx"
df.to_excel(output_file_path, index=False)
