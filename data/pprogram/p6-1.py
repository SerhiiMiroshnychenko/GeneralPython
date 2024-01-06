import pandas as pd

# Зчитуємо дані з файлу sum1.csv
sum1_df = pd.read_csv('/home/smiroshnychenko/Runex3/data/products/extract.csv')

# Зберігаємо дані у файл Excel
sum1_df.to_excel('/home/smiroshnychenko/Runex3/data/products/extract.xls', index=False, engine='openpyxl')
