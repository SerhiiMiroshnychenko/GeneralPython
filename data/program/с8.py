import pandas as pd

# Зчитування даних з файлу sum1.csv
sum1_df = pd.read_csv('sum1.csv')

# Вибірка потрібних полів
sum2_df = sum1_df[["id_imp3", "name_imp3", "property_product_pricelist/id",
                   "property_supplier_payment_term/id", "property_payment_term/id"]]

# Перейменування полів
sum2_df.columns = ["id", "name", "property_product_pricelist/id",
                   "property_supplier_payment_term_id/id", "property_payment_term_id/id"]

# Збереження результатів у файл sum2.csv
sum2_df.to_csv('sum2.csv', index=False)
