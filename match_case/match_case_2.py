def load(link):
    print("Завантажуємо", link)
    return "hello"


def save(link, filename):
    data = load(link)
    print("Зберігаємо в", filename)


def default(values):
    print("Невідомо як обробити")


def old_main(data_string):
    values = data_string.split("~")
    if isinstance(values, (list, tuple)) and len(values) == 2 and values[0] == "load":
        load(values[1])
    elif isinstance(values, (list, tuple)) and len(values) == 3 and values[0] == "save":
        save(values[1], values[2])
    else:
        default(values)


def new_main(data_string):
    values = data_string.split("~")
    match values:
        case "load", link:
            load(link)
        case "save", link, filename:
            save(link, filename)
        case _:
            default(values)


if __name__ == "__main__":
    for word in (
        'load~http://example.com/files/test.txt',
        'save~http://example.com/files/test.txt~file.txt',
        'use~http://example.com/files/test.txt~file.txt',
        'save~http://example.com/files/test.txt~file.txt~file2.txt'
    ):
        print('-'*20)
        old_main(word)
        new_main(word)
