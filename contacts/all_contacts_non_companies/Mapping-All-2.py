import pandas as pd

"""
USER_ID
"""
# Шлях до файлу Excel
file_path_start = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/10001-10462.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(file_path_start)


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
        "__export__.res_users_18": "__export__.res_users_17_e65f7e43",
        False: ""
    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['user_id/id'] = df['user_id/id'].apply(replace_user_id)

# Записуємо змінений DataFrame назад у файл Excel
file_path = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/result-10001-10462.xlsx"
df.to_excel(file_path, index=False)
print('USER_ID')


"""
CHILD_IDS
"""
df = pd.read_excel(file_path)


def replace_child_ids(value):
    replacements = {
        False: ""
    }
    return replacements.get(value, value)


# Замінюємо значення в стовбці user_id/id
df['user_id/id'] = df['user_id/id'].apply(replace_child_ids)

df.to_excel(file_path, index=False)
print('CHILD_IDS')

"""
TAGS
"""
df = pd.read_excel(file_path)


def generate_category(row):
    if row['customer'] and row['supplier']:
        return '__export__.res_partner_category_3_66d8c72e,__export__.res_partner_category_2_506bbdc2'
    elif row['customer']:
        return '__export__.res_partner_category_3_66d8c72e'
    elif row['supplier']:
        return '__export__.res_partner_category_2_506bbdc2'
    else:
        return ''


df['category_id/id'] = df.apply(generate_category, axis=1)

df.to_excel(file_path, index=False)
print('TAGS')


"""
FISCAL POSITION
"""
df = pd.read_excel(file_path)


def replace_fp_id(value):
    replacements = {
        "__export__.account_fiscal_position_8": "l10n_se.1_fp_sweden",
        "__export__.account_fiscal_position_7": "__export__.account_fiscal_position_5_dfa285d5",
        "__export__.account_fiscal_position_1": "__export__.account_fiscal_position_6_ccca4402",
        "__export__.account_fiscal_position_3": "__export__.account_fiscal_position_7_1c713527",
        False: ""

    }
    return replacements.get(value, value)


df['property_account_position/id'] = df['property_account_position/id'].apply(replace_fp_id)

df.to_excel(file_path, index=False)
print('FISCAL POSITION')

"""
PAYMENT TERM
"""
df = pd.read_excel(file_path)


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
        False: ""

    }
    return replacements.get(value, value)


df['property_payment_term/id'] = df['property_payment_term/id'].apply(replace_pt_id)
df['property_supplier_payment_term/id'] = df['property_supplier_payment_term/id'].apply(replace_pt_id)

df.to_excel(file_path, index=False)
print('PAYMENT TERM')

"""
ACCOUNTS
"""
df = pd.read_excel(file_path)

df['property_account_payable/id'] = 'l10n_se.1_a2440'
df['property_account_receivable/id'] = 'l10n_se.1_a1510'

df.to_excel(file_path, index=False)
print('ACCOUNTS')

"""
PRICELIST
"""
df = pd.read_excel(file_path)


def replace_pl_id(value):
    replacements = {
        "purchase.list0": "__export__.product_pricelist_08",
        False: ""
    }
    return replacements.get(value, value)


df['property_product_pricelist_purchase/id'] = df['property_product_pricelist_purchase/id'].apply(replace_pl_id)

df.to_excel(file_path, index=False)
print('PRICELIST')

"""
TYPE
"""
df = pd.read_excel(file_path)


def replace_type_id(value):
    replacements = {
        "Shipping": "Delivery Address",
        "Default": "Contact",
        False: ""
    }
    return replacements.get(value, value)


df['type'] = df['type'].apply(replace_type_id)

df.to_excel(file_path, index=False)
print('TYPE')

"""
COUNTRY_ID
"""
df = pd.read_excel(file_path)


def replace_country(value):
    replacements = {
        False: ""
    }
    return replacements.get(value, value)


df['country_id/id'] = df['country_id/id'].apply(replace_country)

df.to_excel(file_path, index=False)
print('COUNTRY_ID')

"""
SECTION_ID
"""
df = pd.read_excel(file_path)


def replace_section(value):
    replacements = {
        False: ""
    }
    return replacements.get(value, value)


df['section_id/id'] = df['section_id/id'].apply(replace_section)

file_path = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/result-1-2000.xlsx"
df.to_excel(file_path, index=False)
print('SECTION_ID')

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/result-10001-10462.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)

# Замінюємо всі значення False на NaN
df.replace(False, '', inplace=True)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/result-10001-10462-updated.xlsx"
df.to_excel(output_file_path, index=False)

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/result-10001-10462-updated.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)

# Видаляємо рядки, у яких стовбець "id" не заповнений
df.dropna(subset=['id'], inplace=True)

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/all_contacts_non_companies/result-10001-10462-updated-2.xlsx"
df.to_excel(output_file_path, index=False)

print('\nFINISH')
