import pandas as pd


def compare_and_show_matches(file1, file2):
    # Зчитуємо дані з обох файлів у pandas DataFrame
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Визначаємо ключі для порівняння
    keys = ["name", "email", "phone", "mobile", "city"]

    # Об'єднуємо файли за ключами
    merged_df = pd.merge(df1, df2, on=keys, how='inner', suffixes=('_file1', '_file2'))

    # Кількість співпадінь
    matches_count = len(merged_df)

    # Виводимо перші два рядки, якщо є збіги
    if matches_count > 0:
        print("Перші два рядки, що співпали:")
        print(merged_df.head(2))

    return matches_count


if __name__ == "__main__":
    file1 = "/home/smiroshnychenko/Runex3/data/earlier/res.partner.csv"
    file2 = "/home/smiroshnychenko/Runex3/data/earlier/Contact (res.partner) (5).csv"

    matches_count = compare_and_show_matches(file1, file2)

    print(f"Кількість записів, що вдалося співставити: {matches_count}")

