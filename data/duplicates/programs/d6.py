import pandas as pd

# Зчитуємо дані з файлу dname_email_city_create.csv
file_path = "/home/smiroshnychenko/Runex3/data/duplicates/data_files/dname_email_city_create.csv"
df = pd.read_csv(file_path)

# Знаходимо дублікати за полями "Display Name", "Email", "City"
duplicates_df = df[df.duplicated(subset=["Display Name", "Email", "City"], keep=False)]

# Заповнюємо відсутні значення в полях "Email" та "City" пустими рядками
duplicates_df["Email"].fillna("", inplace=True)
duplicates_df["City"].fillna("", inplace=True)

# Створюємо новий DataFrame для dupll.csv
dupll_df = pd.DataFrame(columns=["Display Name", "Email", "City", "Number", "Create"])

# Заповнюємо новий DataFrame
for (name, email, city), group_df in duplicates_df.groupby(["Display Name", "Email", "City"]):
    row_data = {
        "Display Name": name,
        "Email": email,
        "City": city,
        "Number": len(group_df),
        "Create": group_df["Created on"].tolist()
    }
    dupll_df = pd.concat([dupll_df, pd.DataFrame([row_data])], ignore_index=True)

# Записуємо результат у файл dupll.csv
dupll_df.to_csv("/home/smiroshnychenko/Runex3/data/duplicates/data_files/dupll.csv", index=False)
