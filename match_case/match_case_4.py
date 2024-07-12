def main(data_dict):
    match data_dict:
        case {"name": str(name), "access": 1 | 2 as access, "request": request}:
            print(f"Користувач {name} отримав доступ до функції {request} з правами {access}")
        case _:
            print("Невдача")


if __name__ == "__main__":
    for val in (
            {"name": "Daniil", "access": 1, "request": "save"},
            {"name": ["Daniil"], "access": 1, "request": "save"},
            {"name": "Kris", "access": 0, "request": "load"},
    ):
        print('-' * 20)
        main(val)
