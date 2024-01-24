import pandas as pd

# Шлях до CSV-файлу
csv_path = 'res.partner (24).csv'

# Зчитуємо CSV-файл у DataFrame
df = pd.read_csv(csv_path)

# Рахуємо початкову кількість рядків
initial_rows = df.shape[0]

# Видаляємо рядки, де значення одного з полів дорівнює 0, False або відсутнє
df = df[(df['id'] != 0) & (df['partner_product_pricelist/id'].notna()) & (df['partner_product_pricelist/id'] != False)]

# Рахуємо кількість видалених рядків
deleted_rows = initial_rows - df.shape[0]

# Зберігаємо оновлений DataFrame у той же CSV-файл (заміна існуючого файлу)
df.to_csv(csv_path, index=False)

# Виводимо кількість видалених рядків
print(f"Кількість видалених рядків: {deleted_rows}")
