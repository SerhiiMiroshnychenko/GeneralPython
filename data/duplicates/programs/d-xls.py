import pandas as pd

# Зчитуємо дані з файлу sum1.csv
sum1_df = pd.read_csv('/home/smiroshnychenko/Runex3/data/duplicates/data_files/duplicates.csv')

# Зберігаємо дані у файл Excel
sum1_df.to_excel('/home/smiroshnychenko/Runex3/data/duplicates/data_files/duplicates.xls', index=False, engine='openpyxl')
