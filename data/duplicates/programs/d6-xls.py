import pandas as pd

# Зчитуємо дані з файлу sum1.csv
sum1_df = pd.read_csv('dupll.csv')

# Зберігаємо дані у файл Excel
sum1_df.to_excel('dupll.xls', index=False, engine='openpyxl')
