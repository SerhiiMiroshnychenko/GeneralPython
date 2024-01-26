import pandas as pd

# Зчитування файлів
imp2 = pd.read_csv('imp2.csv')
imp3 = pd.read_csv('imp3.csv')

result = pd.merge(imp2, imp3, how='inner', left_on='id_number', right_on='id_number', suffixes=('_imp2', '_imp3'))

# Вибірка потрібних полів для sum1.csv
result_df = result[["id_number", "id_imp2", "id_imp3", "name_imp2", "name_imp3",
                    ]]

# Перейменування полів та збереження результатів
result_df.to_csv('sum1-1.csv', index=False)
