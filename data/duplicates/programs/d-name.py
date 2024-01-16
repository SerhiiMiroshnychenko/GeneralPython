import pandas as pd

# Зчитуємо дані з файлу Contact (res.partner)display_name.csv
file_path = "Contact (res.partner)display_name.csv"
df_contacts = pd.read_csv(file_path)

# Знаходимо дублікати за полем "Display Name"
duplicates_df = df_contacts[df_contacts.duplicated(subset=["Display Name"], keep=False)]

# Створюємо новий DataFrame для dn_dupl.csv
dn_dupl_df = pd.DataFrame(columns=["Display Name", "Number"])

# Заповнюємо новий DataFrame
for name, group_df in duplicates_df.groupby("Display Name"):
    row_data = {"Display Name": name, "Number": len(group_df)}
    dn_dupl_df = pd.concat([dn_dupl_df, pd.DataFrame([row_data])], ignore_index=True)

# Записуємо результат у файл dn_dupl.csv
dn_dupl_df.to_csv("dn_dupl.csv", index=False)
