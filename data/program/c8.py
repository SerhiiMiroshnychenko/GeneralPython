import pandas as pd

# Зчитуємо дані з файлу sum1.csv
sum1_df = pd.read_csv('sum1.csv')

# Зберігаємо дані у файл Excel
sum1_df.to_excel('sum1.xls', index=False, engine='openpyxl')
