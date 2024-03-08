import pandas as pd

# Зчитуємо дані з файлу sum1.csv
sum1_df = pd.read_csv('duplicates2.csv')

# Зберігаємо дані у файл Excel
sum1_df.to_excel('duplicates2.xls', index=False, engine='openpyxl')
