import pandas as pd

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-5.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)


# Функція для заміни значень в стовбці user_id/id
# Замінюємо значення в стовбці user_id/id
df['property_account_payable/id'] = 'l10n_se.1_a2440'
df['property_account_receivable/id'] = 'l10n_se.1_a1510'

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-6.xlsx"
df.to_excel(output_file_path, index=False)
