import pandas as pd

# Шлях до файлу Excel
input_file_path = "c1-2000.xlsx"

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
        "__export__.res_users_420": "__export__.res_users_32_683f998b",
        "__export__.res_users_18": "__export__.res_users_17_e65f7e43"
    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['user_id/id'] = df['user_id/id'].apply(replace_user_id)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "cc1-2000.xlsx"
df.to_excel(output_file_path, index=False)
