import pandas as pd

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES_without_child_ids.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)


# Функція для заміни значень в стовбці user_id/id
def replace_user_id(value):
    replacements = {
        "__export__.res_users_305": "__export__.res_users_9_6845e926",
        "__export__.res_users_7": "__export__.res_users_6_819ac025",
        "__export__.res_users_6": "__export__.res_users_7_fd739659",
        "__export__.res_users_589": "__export__.res_users_30_9f9437c5",
        "__export__.res_users_1158": "__export__.res_users_31_642cf2c9",
        "__export__.res_users_1835": "__export__.res_users_1993",
        "__export__.res_users_420": "__export__.res_users_32_683f998b"
    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['user_id/id'] = df['user_id/id'].apply(replace_user_id)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/companies/COMPANIES-1.xlsx"
df.to_excel(output_file_path, index=False)
