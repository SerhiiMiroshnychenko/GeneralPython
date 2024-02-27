import pandas as pd
import re

# Завантаження даних з Excel файлу
file_path = '/home/smiroshnychenko/Coffee-Project/New-Files/AllProducts.xlsx'
df = pd.read_excel(file_path)


# Функція для виділення даних в квадратних дужках
def extract_data(text):
    match = re.search(r'\[(.*?)\]', text)
    if match:
        return match.group(1)
    else:
        return None


# Оновлення 'Lot/Serial Number' за допомогою даних з квадратних дужок
df['Lot/Serial Number'] = df['Product'].apply(extract_data).fillna(df['Lot/Serial Number'])

# Зберігаємо зміни у файлі
df.to_excel(file_path, index=False)
