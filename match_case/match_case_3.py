def main(data_string):
    values = data_string.split("~")
    match values:
        case name, "1" | "2" as access, request:
            print(f"Користувач {name} отримав доступ до функції {request} з правами {access}")
        case _:
            print("Невдача")


if __name__ == "__main__":
    for word in ('Daniil~2~load', 'Kris~0~save', 'def'):
        print('-' * 20)
        main(word)
