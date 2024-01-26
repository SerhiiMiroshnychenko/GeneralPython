import pandas as pd

# Зчитування файлів
imp2 = pd.read_csv('imp2.csv')
imp3 = pd.read_csv('imp3.csv')

result = pd.merge(imp2, imp3, how='inner', left_on='id_number', right_on='id_number', suffixes=('_imp2', '_imp3'))

# Вибірка потрібних полів для sum1.csv
result_df = result[["id_number", "id_imp3", "name_imp2", "name_imp3",
                    "property_product_pricelist_purchase/id", "property_product_pricelist/id",
                    "property_supplier_payment_term/id", "property_supplier_payment_term_id/id",
                    "property_payment_term/id", "property_payment_term_id/id"]]

# Перейменування полів та збереження результатів
result_df.to_csv('sum1.csv', index=False)
