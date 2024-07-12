class UserRequest:
    __match_args__ = ('name', 'access', 'request')

    def __init__(self, name, access, request):
        self.name = name
        self.access = access
        self.request = request


def main(data_class):
    match data_class:
        case UserRequest(_, _, request) if request["func"] == "delete" and request["directory"] == "main_folder":
            print(f"Заборонено видаляти файли з {request['directory']}")
        case UserRequest(str(name), 1 | 2 as access, request):
            print(f"Користувач {name} отримав доступ до функції {request} з правами {access}")
        case _:
            print("Невдача")


if __name__ == "__main__":
    for val in (
        UserRequest("Daniil", 1, {"func": "delete", "file": "test.txt", "directory": "main_folder"}),
        UserRequest("Daniil", 1, {"func": "save", "file": "test.txt", "directory": "main_folder"})
    ):
        print('-' * 20)
        main(val)
