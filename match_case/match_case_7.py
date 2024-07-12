class UserRequest:
    __match_args__ = ('name', 'access', 'request')

    def __init__(self, name, access, request):
        print("Створений новий UserRequest")
        self.name = name
        self.access = access
        self.request = request


def main(data_class):
    match data_class:
        case UserRequest(str(name), 1 | 2 as access, request):
            print(f"Користувач {name} отримав доступ до функції {request} з правами {access}")
        case _:
            print("Невдача")


if __name__ == "__main__":
    for val in (
            UserRequest("Daniil", 1, "delete"),
    ):
        print('-' * 20)
        main(val)
