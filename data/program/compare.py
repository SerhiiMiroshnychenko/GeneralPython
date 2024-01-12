import pandas as pd


def compare_and_count_matches(file1, file2):
    # Зчитуємо дані з обох файлів у pandas DataFrame
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Визначаємо ключі для порівняння
    keys = ["name", "email", "phone", "mobile", "city"]

    # Об'єднуємо файли за ключами
    merged_df = pd.merge(df1, df2, on=keys, how='inner', suffixes=('_file1', '_file2'))

    # Кількість співпадінь
    matches_count = len(merged_df)

    return matches_count


if __name__ == "__main__":
    file1 = "res.partner.csv"
    file2 = "Contact (res.partner) (5).csv"

    matches_count = compare_and_count_matches(file1, file2)

    print(f"Кількість записів, що вдалося співставити: {matches_count}")
