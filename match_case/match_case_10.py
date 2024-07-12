# python match case with OR operator
def run_match():
    num = int(input("Enter a number between 1 and 6: "))

    # match case
    match num:
        # pattern 1
        case 1 | 2:
            print("One or Two")
        # pattern 2
        case 3 | 4:
            print("Three or Four")
        # pattern 3
        case 5 | 6:
            print("Five or Six")
        # default pattern
        case _:
            print("Number not between 1 and 6")


if __name__ == "__main__":
    run_match()

