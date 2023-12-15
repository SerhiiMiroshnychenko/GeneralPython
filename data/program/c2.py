import pandas as pd

# Зчитування файлів
file1 = "/home/smiroshnychenko/Runex3/data/earlier/res.partner.csv"
file2 = "/home/smiroshnychenko/Runex3/data/earlier/Contact (res.partner) (5).csv"


df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Створення списку для зберігання результатів
result = []
res = []
counter = 0

# Порівняння кожного рядка df1 з кожним рядком df2
for index1, row1 in df1.iterrows():
    print(counter)
    for index2, row2 in df2.iterrows():
        # Порівняння значень полів "name", "email", "phone", "mobile", "city"
        if (row1['name'] == row2['name'] and
                row1['email'] == row2['email'] and
                row1['phone'] == row2['phone'] and
                row1['mobile'] == row2['mobile'] and
                row1['city'] == row2['city']):
            # Запис пари "id" в результат
            result.append((row1['id'], row2['id']))
            # Додавання пари "id" до результату
            res.append({'old_id': row1['id'], 'new_id': row2['id']})
    counter += 1

# Створення DataFrame з результатами
result_df = pd.DataFrame(res, columns=['old_id', 'new_id'])

# Запис результатів у файл result.csv
result_df.to_csv('/home/smiroshnychenko/Runex3/data/earlier/result.csv', index=False)

# Виведення результатів
print(len(result))
