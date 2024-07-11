def load():
    print("Завантажуємо")


def save():
    print("Зберігаємо")


def default():
    print("Невідомо як обробити")


def old_main(value):
    if isinstance(value, str) and value == "load":
        load()
    elif isinstance(value, str) and value == "save":
        save()
    else:
        default()


def new_main(value):
    match value:
        case "load":
            load()
        case "save":
            save()
        case _:
            default()


if __name__ == "__main__":
    for word in ('load', 'save', 'def'):
        print('-'*20)
        old_main(word)
        new_main(word)
