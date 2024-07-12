# match case to check a character in a string
def run_match():
    my_str = "Hello World"

    # match case
    match (my_str[6]):
        case "w":
            print("Case 1 matches")
        case "W":
            print("Case 2 matches")
        case _:
            print("Character not in the string")


if __name__ == "__main__":
    run_match()

