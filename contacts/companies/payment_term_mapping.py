import pandas as pd

# Шлях до файлу Excel
input_file_path = "COMPANIES-3.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)


# Функція для заміни значень в стовбці user_id/id
def replace_pt_id(value):
    replacements = {
        "__export__.account_payment_term_8": "__export__.account_payment_term_11_f3911377",
        "__export__.account_payment_term_9": "__export__.account_payment_term_14_5f6e8180",
        "__export__.account_payment_term_10": "__export__.account_payment_term_15_3fe21092",
        "__export__.account_payment_term_4": "account.account_payment_term_21days",
        "account.account_payment_term_net": "account.account_payment_term_30days",
        "__export__.account_payment_term_5": "account.account_payment_term_45days",
        "__export__.account_payment_term_6": "__export__.account_payment_term_12_d221589a",
        "__export__.account_payment_term_7": "__export__.account_payment_term_13_d46e44c0",
        "__export__.account_payment_term_14": "__export__.account_payment_term_16_524a4bb6",
        "__export__.account_payment_term_13": "__export__.account_payment_term_17_e7522fe8",
        "__export__.account_payment_term_12": "__export__.account_payment_term_18_d169baa6",
        "__export__.account_payment_term_11": "__export__.account_payment_term_19_cdc89246",

    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['property_payment_term/id'] = df['property_payment_term/id'].apply(replace_pt_id)
df['property_supplier_payment_term/id'] = df['property_supplier_payment_term/id'].apply(replace_pt_id)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "COMPANIES-4.xlsx"
df.to_excel(output_file_path, index=False)
