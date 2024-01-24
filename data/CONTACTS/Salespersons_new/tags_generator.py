import pandas as pd

# Шлях до файлу Excel
excel_file_path = "Tags_and_company.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(excel_file_path)


# Функція для генерації значення category_id/id
def generate_category(row):
    if row['is_customer'] and row['is_supplier']:
        return '__export__.res_partner_category_3_66d8c72e,__export__.res_partner_category_2_506bbdc2'
    elif row['is_customer']:
        return '__export__.res_partner_category_3_66d8c72e'
    elif row['is_supplier']:
        return '__export__.res_partner_category_2_506bbdc2'
    else:
        return ''


# Застосовуємо функцію до кожного рядка
df['category_id/id'] = df.apply(generate_category, axis=1)

# Записуємо змінений DataFrame назад у файл Excel
df.to_excel("Tags_and_company_modified.xlsx", index=False)
