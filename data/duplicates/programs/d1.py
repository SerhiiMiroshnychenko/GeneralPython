import pandas as pd

# Зчитуємо дані з файлу
file_path = "Contact (res.partner) (9).csv"
df = pd.read_csv(file_path)

# Знаходимо дублікати за полями "name" та "email"
duplicates_df = df[df.duplicated(subset=["name", "email"], keep=False)]

# Створюємо новий DataFrame для duplicates.csv
duplicates_result_df = pd.DataFrame(columns=["name", "email", "id 1", "id 2"])

# Заповнюємо новий DataFrame
for (name, email), group_df in duplicates_df.groupby(["name", "email"]):
    ids = group_df["id"].tolist()
    row_data = {"name": name, "email": email, "id 1": ids[0], "id 2": ids[1] if len(ids) > 1 else None}
    duplicates_result_df = pd.concat([duplicates_result_df, pd.DataFrame([row_data])], ignore_index=True)

# Записуємо результат у файл duplicates.csv
duplicates_result_df.to_csv("duplicates.csv", index=False)

