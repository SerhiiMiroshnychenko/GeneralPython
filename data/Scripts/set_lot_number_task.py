import pandas as pd
import re

# Завантажуємо дані з Excel файлу
file_path = '/home/smiroshnychenko/Coffee-Project/FTR/FTR-task (копія).xlsx'
df = pd.read_excel(file_path)


# Функція для виділення даних в дужках
def extract_data(text):
    match = re.search(r'\((.*?)\)', text)
    if match:
        return match.group(1)
    else:
        return None


# Застосовуємо функцію до стовбця 'Product' і створюємо новий стовбець 'Lot/Serial Number'
df['Lot/Serial Number'] = df['Product'].apply(lambda x: extract_data(x))

# Зберігаємо зміни у файлі
df.to_excel(file_path, index=False)
