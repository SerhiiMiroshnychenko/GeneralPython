import pandas as pd
import re

# Зчитування файлу res.partner.csv
file_path = "res.partner.csv"
df = pd.read_csv(file_path)


# Функція для видобуття перших п'яти цифр з поля "id"
def extract_id_number(row):
    match = re.search(r'\d{5}|\d{4}|\d{3}', str(row['id']))
    return int(match.group()) if match else None


# Додавання нового стовпця "id_number"
df['id_number'] = df.apply(extract_id_number, axis=1)

# Вибірка потрібних полів для imp.csv
selected_columns = ['id_number', 'id', 'name', 'email', 'phone', 'mobile', 'city',
                    'property_product_pricelist_purchase/id', 'property_supplier_payment_term/id',
                    'property_payment_term/id']
df_imp = df[selected_columns]

# Запис у файл imp.csv
df_imp.to_csv('imp2.csv', index=False)
