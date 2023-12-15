import pandas as pd

# Шлях до файлу Excel
input_file_path = "/home/smiroshnychenko/GeneralPython/contacts/childs_id/ChildsID-2.xlsx"

# Зчитуємо дані з Excel
df = pd.read_excel(input_file_path)

# Видаляємо рядки, в яких значення стовпця 'child_ids/id' дорівнює False
df = df[df['child_ids/id'] != False]

# Записуємо змінений DataFrame назад у файл Excel
output_file_path = "/home/smiroshnychenko/GeneralPython/contacts/childs_id/ChildsID-2-updated.xlsx"
df.to_excel(output_file_path, index=False)
