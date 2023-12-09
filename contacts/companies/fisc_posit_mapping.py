import pandas as pd

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-2.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)


# Функція для заміни значень в стовбці user_id/id
def replace_fp_id(value):
    replacements = {
        "__export__.account_fiscal_position_8": "l10n_se.1_fp_sweden",
        "__export__.account_fiscal_position_7": "__export__.account_fiscal_position_5_dfa285d5",
        "__export__.account_fiscal_position_1": "__export__.account_fiscal_position_6_ccca4402",
        "__export__.account_fiscal_position_3": "__export__.account_fiscal_position_7_1c713527",

    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['property_account_position/id'] = df['property_account_position/id'].apply(replace_fp_id)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-3.xlsx"
df.to_excel(output_file_path, index=False)
