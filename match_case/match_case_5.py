class UserRequest:
    def __init__(self, name, access, request):
        self.name = name
        self.access = access
        self.request = request


def main(data_class):
    match data_class:
        case UserRequest(name=str(name), access=1 | 2 as access, request=request):
            print(f"Користувач {name} отримав доступ до функції {request} з правами {access}")
        case _:
            print("Невдача")


if __name__ == "__main__":
    for val in (
            UserRequest("Daniil", 1, "delete"),
            UserRequest(1234, 1, "delete"),
            UserRequest("Kris", 0, "save"),
    ):
        print('-' * 20)
        main(val)
